/**
 * Typing Effect Module for About Section
 */
export class TypingEffect {
    constructor(elementId, options = {}) {
        this.element = document.getElementById(elementId);
        if (!this.element) return;

        this.text = options.text || '';
        this.speed = options.speed || 50;
        this.delay = options.delay || 500;
        this.currentIndex = 0;
        this.hasStarted = false;
        
        this.init();
    }

    init() {
        // Use Intersection Observer to start typing when in view
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !this.hasStarted) {
                    this.hasStarted = true;
                    setTimeout(() => {
                        this.type();
                    }, this.delay);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        // Observe the parent element since the span itself might be empty/small
        if (this.element.parentElement) {
            observer.observe(this.element.parentElement);
        } else {
            observer.observe(this.element);
        }
    }

    type() {
        if (this.currentIndex < this.text.length) {
            this.element.textContent += this.text.charAt(this.currentIndex);
            this.currentIndex++;
            setTimeout(() => this.type(), this.speed);
        }
    }

    reset() {
        this.element.textContent = '';
        this.currentIndex = 0;
        this.hasStarted = false;
    }
}

// Auto-initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const typingElement = document.getElementById('typing-text');
    if (typingElement) {
        new TypingEffect('typing-text', {
            text: 'Building intelligent AI/ML systems that transform data into insights, automate complex workflows, and deliver production-ready solutions at scale.',
            speed: 40,
            delay: 300
        });
    }
});
