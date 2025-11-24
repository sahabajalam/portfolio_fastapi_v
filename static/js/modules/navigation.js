/**
 * Optimized Navigation Module - Consolidated navigation functionality
 * Uses centralized Utils module for common functions
 */
import Utils from './utils.js';

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
            link.addEventListener('click', (e) => {
                closeMobileMenu();
                
                // Enhanced mobile navigation: Scroll to top if clicking current page
                const href = link.getAttribute('href');
                const currentPath = window.location.pathname;
                
                // Check if it's a link to the current page without a hash
                if (href === currentPath || (href === '/' && currentPath === '/index.html')) {
                    // If it's the NoteonAI page, we might want to reset filters or scroll to top
                    if (href.includes('noteonai')) {
                        // Let default behavior happen (reload) to reset state, 
                        // or prevent default and scroll to top if preferred.
                        // For now, we'll let it reload to ensure clean state.
                    } else {
                        // For other pages, scroll to top is nice
                        window.scrollTo({ top: 0, behavior: 'smooth' });
                    }
                }
            });
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
                        // Use centralized Utils method for smooth scrolling
                        Utils.smoothScrollTo(targetId, 20);
                    } else {
                        // Navigate to home page with hash if we're not on home page
                        const currentPath = window.location.pathname;
                        if (currentPath !== '/' && currentPath !== '/index.html') {
                            window.location.href = targetId === 'home' ? '/' : `/#${targetId}`;
                        }
                    }
                }
            });
        });
    }

    setupScrollEffects() {
        const navbar = document.querySelector('.navbar');
        if (!navbar) return;

        // Use centralized throttled scroll handler for performance
        const throttledScrollHandler = Utils.throttle(() => {
            const currentScrollY = window.scrollY;
            navbar.classList.toggle('scrolled', currentScrollY > 50);
        }, 16); // ~60fps

        window.addEventListener('scroll', throttledScrollHandler);
    }

    setupActiveLinks() {
        // Use centralized Utils method
        Utils.setupActiveLinks('.nav-link[data-section]', 'section[id]', {
            threshold: 0.3,
            rootMargin: '-100px 0px -100px 0px'
        });
    }

    handleHashOnLoad() {
        window.addEventListener('load', () => {
            const hash = window.location.hash;
            if (hash) {
                const targetId = hash.substring(1);
                // Use centralized Utils method for smooth scrolling
                setTimeout(() => {
                    Utils.smoothScrollTo(targetId, 20);
                }, 100);
            }
        });
    }
}
