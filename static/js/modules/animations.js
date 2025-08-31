/**
 * Animation and UI Effects Module
 */
export class AnimationManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupScrollAnimations();
        this.setupSkillsScrollFade();
        this.setupCertificationsScrollFade();
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

    setupSkillsScrollFade() {
        const container = document.getElementById('skills-container');
        const fadeTop = document.getElementById('skills-fade-top');
        const fadeBottom = document.getElementById('skills-fade-bottom');

        if (!container || !fadeTop || !fadeBottom) return;

        container.addEventListener('scroll', () => {
            const { scrollTop, scrollHeight, clientHeight } = container;

            // Show/hide top fade
            if (scrollTop > 10) {
                fadeTop.style.opacity = '1';
            } else {
                fadeTop.style.opacity = '0';
            }

            // Show/hide bottom fade
            if (scrollTop < scrollHeight - clientHeight - 10) {
                fadeBottom.style.opacity = '1';
            } else {
                fadeBottom.style.opacity = '0';
            }
        });
    }

    setupCertificationsScrollFade() {
        const container = document.getElementById('certifications-container');
        const fadeTop = document.getElementById('cert-fade-top');
        const fadeBottom = document.getElementById('cert-fade-bottom');

        if (!container || !fadeTop || !fadeBottom) return;

        container.addEventListener('scroll', () => {
            const { scrollTop, scrollHeight, clientHeight } = container;

            // Show/hide top fade
            if (scrollTop > 5) {
                fadeTop.style.opacity = '1';
            } else {
                fadeTop.style.opacity = '0';
            }

            // Show/hide bottom fade
            if (scrollTop < scrollHeight - clientHeight - 5) {
                fadeBottom.style.opacity = '1';
            } else {
                fadeBottom.style.opacity = '0';
            }
        });
    }
}

/**
 * Utility Functions Module
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
}

// Global utility functions for backward compatibility
window.scrollToTop = Utils.scrollToTop;
