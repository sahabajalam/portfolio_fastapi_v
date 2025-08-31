/**
 * Optimized Animation and UI Effects Module
 * Consolidated scroll fade functionality and removed duplications
 */
export class AnimationManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupScrollAnimations();
        this.setupScrollFadeContainers();
    }

    setupScrollAnimations() {
        const animatedElements = document.querySelectorAll('.animate-on-load');

        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);

        animatedElements.forEach(element => {
            observer.observe(element);
        });
    }

    /**
     * Universal scroll fade handler - eliminates duplication
     * @param {string} containerId - ID of the scrollable container
     * @param {string} fadeTopId - ID of the top fade element
     * @param {string} fadeBottomId - ID of the bottom fade element
     * @param {number} threshold - Scroll threshold for fade trigger
     */
    setupScrollFade(containerId, fadeTopId, fadeBottomId, threshold = 10) {
        const container = document.getElementById(containerId);
        const fadeTop = document.getElementById(fadeTopId);
        const fadeBottom = document.getElementById(fadeBottomId);

        if (!container || !fadeTop || !fadeBottom) return;

        container.addEventListener('scroll', () => {
            const { scrollTop, scrollHeight, clientHeight } = container;

            // Show/hide top fade
            fadeTop.style.opacity = scrollTop > threshold ? '1' : '0';

            // Show/hide bottom fade
            fadeBottom.style.opacity = 
                scrollTop < scrollHeight - clientHeight - threshold ? '1' : '0';
        });
    }

    /**
     * Setup all scroll fade containers from configuration
     */
    setupScrollFadeContainers() {
        const containers = [
            {
                container: 'skills-container',
                fadeTop: 'skills-fade-top',
                fadeBottom: 'skills-fade-bottom',
                threshold: 10
            },
            {
                container: 'certifications-container',
                fadeTop: 'cert-fade-top',
                fadeBottom: 'cert-fade-bottom',
                threshold: 5
            }
        ];

        containers.forEach(config => {
            this.setupScrollFade(
                config.container,
                config.fadeTop,
                config.fadeBottom,
                config.threshold
            );
        });
    }
}

/**
 * Optimized Utility Functions Module
 */
export class Utils {
    static scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    static debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    static throttle(func, limit) {
        let inThrottle;
        return function () {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }

    /**
     * Universal smooth scroll to element
     * @param {string} targetId - ID of target element
     * @param {number} offset - Additional offset from top
     */
    static smoothScrollTo(targetId, offset = 20) {
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
            const targetPosition = targetElement.offsetTop - navHeight - offset;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    }
}

// Global utility functions for backward compatibility
window.scrollToTop = Utils.scrollToTop;
