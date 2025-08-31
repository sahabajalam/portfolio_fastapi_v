/**
 * Navigation Module - Handles all navigation-related functionality
 */
export class NavigationManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupMobileMenu();
        this.setupSmoothScrolling();
        this.setupScrollEffects();
        this.setupActiveLinks();
        this.handleHashOnLoad();
    }

    setupMobileMenu() {
        const hamburger = document.querySelector('.navbar-mobile-menu-toggle');
        const mobileMenu = document.querySelector('.mobile-menu');

        if (hamburger && mobileMenu) {
            const toggleMobileMenu = () => {
                const isActive = mobileMenu.classList.contains('active');
                if (isActive) {
                    mobileMenu.classList.remove('active');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    document.body.style.overflow = '';
                } else {
                    mobileMenu.classList.add('active');
                    hamburger.classList.add('active');
                    hamburger.setAttribute('aria-expanded', 'true');
                    document.body.style.overflow = 'hidden';
                }
            };

            hamburger.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                toggleMobileMenu();
            });

            // Close mobile menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
                    mobileMenu.classList.remove('active');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    document.body.style.overflow = '';
                }
            });

            // Close mobile menu when clicking on a link
            const mobileLinks = mobileMenu.querySelectorAll('a');
            mobileLinks.forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.remove('active');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    document.body.style.overflow = '';
                });
            });
        }
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
                        // Target element exists on current page - smooth scroll to it
                        const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
                        const targetPosition = targetElement.offsetTop - navHeight - 20;

                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    } else {
                        // Target element doesn't exist - navigate to home page with hash
                        const currentPath = window.location.pathname;
                        if (currentPath !== '/' && currentPath !== '/index.html') {
                            // We're not on the home page, redirect to home with the section hash
                            window.location.href = `/#${targetId}`;
                        }
                    }
                }
            });
        });
    }

    setupScrollEffects() {
        const navbar = document.querySelector('.navbar');
        if (!navbar) return;

        let lastScrollY = window.scrollY;

        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;

            // Add/remove scrolled class
            if (currentScrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            lastScrollY = currentScrollY;
        });
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
                    const sectionId = entry.target.id;

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
            });
        }, observerOptions);

        sections.forEach(section => observer.observe(section));
    }

    handleHashOnLoad() {
        // Handle hash navigation when page loads
        window.addEventListener('load', () => {
            const hash = window.location.hash;
            if (hash) {
                const targetId = hash.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    // Wait a bit for the page to fully load, then scroll
                    setTimeout(() => {
                        const navHeight = document.querySelector('.navbar')?.offsetHeight || 0;
                        const targetPosition = targetElement.offsetTop - navHeight - 20;

                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }, 100);
                }
            }
        });
    }
}
