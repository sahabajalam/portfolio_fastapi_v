/**
 * Optimized Animation and UI Effects Module
 * Consolidated scroll fade functionality and removed duplications
 * Uses centralized Utils module for common functions
 */
import Utils from './utils.js';

export class AnimationManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupScrollAnimations();
        this.setupScrollFadeContainers();
    }

    setupScrollAnimations() {
        // Use centralized Utils method
        Utils.setupScrollAnimations('.animate-on-load', {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
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
            Utils.setupScrollFade(
                config.container,
                config.fadeTop,
                config.fadeBottom,
                config.threshold
            );
        });
    }
}

// Re-export Utils for backward compatibility
export { Utils };
