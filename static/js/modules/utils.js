/**
 * Centralized Utility Functions Module
 * Eliminates duplication across animation.js, navigation.js, and other modules
 */

export class Utils {
    /**
     * Throttle function execution
     * @param {Function} func - Function to throttle
     * @param {number} limit - Time limit in milliseconds
     * @returns {Function} Throttled function
     */
    static throttle(func, limit) {
        let inThrottle;
        return function (...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    /**
     * Debounce function execution
     * @param {Function} func - Function to debounce
     * @param {number} wait - Wait time in milliseconds
     * @returns {Function} Debounced function
     */
    static debounce(func, wait) {
        let timeout;
        return function (...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    /**
     * Universal smooth scroll to element
     * @param {string} targetId - ID of target element
     * @param {number} offset - Additional offset from top (default: 20)
     */
    static smoothScrollTo(targetId, offset = 20) {
        const targetElement = document.getElementById(targetId);
        if (!targetElement) return;

        const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
        const targetPosition = targetElement.offsetTop - navHeight - offset;

        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }

    /**
     * Scroll to top of page
     */
    static scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    /**
     * Universal scroll fade handler for containers
     * @param {string} containerId - ID of the scrollable container
     * @param {string} fadeTopId - ID of the top fade element
     * @param {string} fadeBottomId - ID of the bottom fade element
     * @param {number} threshold - Scroll threshold for fade trigger (default: 10)
     */
    static setupScrollFade(containerId, fadeTopId, fadeBottomId, threshold = 10) {
        const container = document.getElementById(containerId);
        const fadeTop = document.getElementById(fadeTopId);
        const fadeBottom = document.getElementById(fadeBottomId);

        if (!container || !fadeTop || !fadeBottom) return;

        const handleScroll = () => {
            const { scrollTop, scrollHeight, clientHeight } = container;
            fadeTop.style.opacity = scrollTop > threshold ? '1' : '0';
            fadeBottom.style.opacity = scrollTop < scrollHeight - clientHeight - threshold ? '1' : '0';
        };

        container.addEventListener('scroll', handleScroll);
        return () => container.removeEventListener('scroll', handleScroll);
    }

    /**
     * Setup Intersection Observer for animations
     * @param {string} selector - CSS selector for elements to observe
     * @param {Object} options - Observer options
     * @returns {IntersectionObserver} Observer instance
     */
    static setupScrollAnimations(selector = '.animate-on-load', options = {}) {
        const defaultOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px',
            ...options
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, defaultOptions);

        document.querySelectorAll(selector).forEach(element => {
            observer.observe(element);
        });

        return observer;
    }

    /**
     * Setup active link tracking based on scroll position
     * @param {string} linkSelector - CSS selector for navigation links
     * @param {string} sectionSelector - CSS selector for sections
     * @param {Object} options - Observer options
     */
    static setupActiveLinks(linkSelector = '.nav-link[data-section]', sectionSelector = 'section[id]', options = {}) {
        const navLinks = document.querySelectorAll(linkSelector);
        const sections = document.querySelectorAll(sectionSelector);

        if (sections.length === 0) return;

        const defaultOptions = {
            threshold: 0.3,
            rootMargin: '-100px 0px -100px 0px',
            ...options
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    Utils.updateActiveLink(entry.target.id, navLinks);
                }
            });
        }, defaultOptions);

        sections.forEach(section => observer.observe(section));
        return observer;
    }

    /**
     * Update active navigation link
     * @param {string} sectionId - ID of the active section
     * @param {NodeList} navLinks - Navigation links to update
     */
    static updateActiveLink(sectionId, navLinks) {
        navLinks.forEach(link => link.parentElement.classList.remove('active'));
        const activeLink = document.querySelector(`.nav-link[data-section="${sectionId}"]`);
        if (activeLink) activeLink.parentElement.classList.add('active');
    }

    /**
     * Generic DOM element creation helper
     * @param {string} tag - HTML tag name
     * @param {Object} attributes - Element attributes
     * @param {string|Node|Array} content - Element content
     * @returns {HTMLElement} Created element
     */
    static createElement(tag, attributes = {}, content = null) {
        const element = document.createElement(tag);

        Object.entries(attributes).forEach(([key, value]) => {
            if (key === 'class') {
                element.className = value;
            } else if (key === 'style' && typeof value === 'object') {
                Object.assign(element.style, value);
            } else if (key.startsWith('data-')) {
                element.dataset[key.slice(5)] = value;
            } else {
                element.setAttribute(key, value);
            }
        });

        if (content) {
            if (typeof content === 'string') {
                element.innerHTML = content;
            } else if (Array.isArray(content)) {
                content.forEach(child => element.appendChild(child));
            } else if (content instanceof Node) {
                element.appendChild(content);
            }
        }

        return element;
    }

    /**
     * Check if element is in viewport
     * @param {HTMLElement} element - Element to check
     * @returns {boolean} True if element is in viewport
     */
    static isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    /**
     * Get computed CSS variable value
     * @param {string} variableName - CSS variable name (with or without --)
     * @returns {string} Variable value
     */
    static getCSSVariable(variableName) {
        const name = variableName.startsWith('--') ? variableName : `--${variableName}`;
        return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    }

    /**
     * Set CSS variable value
     * @param {string} variableName - CSS variable name (with or without --)
     * @param {string} value - Variable value
     */
    static setCSSVariable(variableName, value) {
        const name = variableName.startsWith('--') ? variableName : `--${variableName}`;
        document.documentElement.style.setProperty(name, value);
    }
}

// Global utility functions for backward compatibility
if (typeof window !== 'undefined') {
    window.scrollToTop = Utils.scrollToTop.bind(Utils);
    window.smoothScrollTo = Utils.smoothScrollTo.bind(Utils);
}

export default Utils;
