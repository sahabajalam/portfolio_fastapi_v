/**
 * Optimized Navigation Module - Consolidated navigation functionality
 */
export class NavigationManager {
    constructor() {
        this.mobileMenuState = false;
        this.init();
    }

    init() {
        this.setupMobileMenu();
        this.setupSmoothScrolling();
        this.setupScrollEffects();
        this.setupActiveLinks();
        this.handleHashOnLoad();
    }

    /**
     * Optimized mobile menu with centralized state management
     */
    setupMobileMenu() {
        const hamburger = document.querySelector('.navbar-mobile-menu-toggle');
        const mobileMenu = document.querySelector('.mobile-menu');

        if (!hamburger || !mobileMenu) return;

        const toggleMobileMenu = () => {
            this.mobileMenuState = !this.mobileMenuState;
            this.updateMobileMenuUI(hamburger, mobileMenu);
        };

        const closeMobileMenu = () => {
            if (this.mobileMenuState) {
                this.mobileMenuState = false;
                this.updateMobileMenuUI(hamburger, mobileMenu);
            }
        };

        // Event listeners
        hamburger.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            toggleMobileMenu();
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
                closeMobileMenu();
            }
        });

        // Close on mobile link click
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }

    /**
     * Update mobile menu UI state
     */
    updateMobileMenuUI(hamburger, mobileMenu) {
        const method = this.mobileMenuState ? 'add' : 'remove';
        
        mobileMenu.classList[method]('active');
        hamburger.classList[method]('active');
        hamburger.setAttribute('aria-expanded', this.mobileMenuState);
        document.body.style.overflow = this.mobileMenuState ? 'hidden' : '';
    }

    setupSmoothScrolling() {
        const navLinks = document.querySelectorAll('a[href^="#"], a[data-section]');

        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                const section = link.getAttribute('data-section');
                const targetId = section || (href && href.startsWith('#') ? href.substring(1) : null);

                if (targetId) {
                    e.preventDefault();
                    const targetElement = document.getElementById(targetId);

                    if (targetElement) {
                        // Use Utils for consistent smooth scrolling
                        const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
                        const targetPosition = targetElement.offsetTop - navHeight - 20;

                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    } else {
                        // Navigate to home page with hash
                        const currentPath = window.location.pathname;
                        if (currentPath !== '/' && currentPath !== '/index.html') {
                            window.location.href = `/${href}`;
                        }
                    }
                }
            });
        });
    }

    setupScrollEffects() {
        const navbar = document.querySelector('.navbar');
        if (!navbar) return;

        // Use throttled scroll handler for performance
        const throttledScrollHandler = this.throttle(() => {
            const currentScrollY = window.scrollY;
            navbar.classList.toggle('scrolled', currentScrollY > 50);
        }, 16); // ~60fps

        window.addEventListener('scroll', throttledScrollHandler);
    }

    setupActiveLinks() {
        const navLinks = document.querySelectorAll('.nav-link[data-section]');
        const sections = document.querySelectorAll('section[id]');

        if (sections.length === 0) return;

        const observerOptions = {
            threshold: 0.3,
            rootMargin: '-100px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.updateActiveLink(entry.target.id, navLinks);
                }
            });
        }, observerOptions);

        sections.forEach(section => observer.observe(section));
    }

    /**
     * Update active navigation link
     */
    updateActiveLink(sectionId, navLinks) {
        // Remove active class from all links
        navLinks.forEach(link => {
            link.parentElement.classList.remove('active');
        });

        // Add active class to current link
        const activeLink = document.querySelector(`.nav-link[data-section="${sectionId}"]`);
        if (activeLink) {
            activeLink.parentElement.classList.add('active');
        }
    }

    handleHashOnLoad() {
        window.addEventListener('load', () => {
            const hash = window.location.hash;
            if (hash) {
                const targetId = hash.substring(1);
                // Use Utils for consistent smooth scrolling
                setTimeout(() => {
                    const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
                    const targetPosition = targetElement.offsetTop - navHeight - 20;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }, 100);
            }
        });
    }

    /**
     * Simple throttle implementation
     */
    throttle(func, limit) {
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
}
