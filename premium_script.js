// Premium Frontend JavaScript with Modern Technologies
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize premium features
    initializePremiumFeatures();
    
    // Smooth scrolling with premium easing
    initializeSmoothScrolling();
    
    // Premium header effects
    initializeHeaderEffects();
    
    // Intersection Observer for premium animations
    initializeIntersectionObserver();
    
    // Premium form enhancements
    initializeFormEnhancements();
    
    // Premium contact interactions
    initializeContactInteractions();
    
    // Premium image lazy loading
    initializeLazyLoading();
    
    // Premium back to top button
    initializeBackToTop();
    
    // Premium performance optimizations
    initializePerformanceOptimizations();
    
    // Premium hover effects
    initializeHoverEffects();
    
    console.log('🎨 Premium Legacy Estates website loaded successfully');
});

function initializePremiumFeatures() {
    // Add loading states
    document.body.classList.add('premium-loaded');
    
    // Initialize CSS custom properties for dynamic theming
    const root = document.documentElement;
    root.style.setProperty('--scroll-progress', '0%');
}

function initializeSmoothScrolling() {
    // Premium smooth scrolling with custom easing
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const targetPosition = target.offsetTop - 100;
                const startPosition = window.pageYOffset;
                const distance = targetPosition - startPosition;
                const duration = 1000;
                let start = null;
                
                function animation(currentTime) {
                    if (start === null) start = currentTime;
                    const timeElapsed = currentTime - start;
                    const run = easeInOutCubic(timeElapsed, startPosition, distance, duration);
                    window.scrollTo(0, run);
                    if (timeElapsed < duration) requestAnimationFrame(animation);
                }
                
                requestAnimationFrame(animation);
            }
        });
    });
    
    // Custom easing function
    function easeInOutCubic(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t * t + b;
        t -= 2;
        return c / 2 * (t * t * t + 2) + b;
    }
}

function initializeHeaderEffects() {
    const header = document.querySelector('.header');
    let lastScroll = 0;
    let ticking = false;
    
    function updateHeader() {
        const currentScroll = window.pageYOffset;
        
        // Add scroll progress to CSS custom property
        const scrollProgress = (currentScroll / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
        document.documentElement.style.setProperty('--scroll-progress', `${scrollProgress}%`);
        
        // Header hide/show effect
        if (currentScroll > lastScroll && currentScroll > 100) {
            header.style.transform = 'translateY(-100%)';
            header.style.opacity = '0.8';
        } else {
            header.style.transform = 'translateY(0)';
            header.style.opacity = '1';
        }
        
        // Add glass effect based on scroll
        if (currentScroll > 50) {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(20px)';
        } else {
            header.style.background = 'rgba(255, 255, 255, 0.8)';
            header.style.backdropFilter = 'blur(10px)';
        }
        
        lastScroll = currentScroll;
        ticking = false;
    }
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateHeader);
            ticking = true;
        }
    });
}

function initializeIntersectionObserver() {
    // Premium intersection observer with multiple animation types
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add different animation classes based on element type
                const element = entry.target;
                
                if (element.classList.contains('feature-item')) {
                    element.style.animation = 'slideInUp 0.8s ease-out forwards';
                } else if (element.classList.contains('hero-content')) {
                    element.style.animation = 'fadeInUp 1s ease-out forwards';
                } else {
                    element.classList.add('fade-in', 'visible');
                }
                
                // Add staggered animations for child elements
                const children = element.querySelectorAll('.feature-icon, .feature-text');
                children.forEach((child, index) => {
                    child.style.animationDelay = `${index * 0.1}s`;
                    child.style.animation = 'fadeInUp 0.6s ease-out forwards';
                });
            }
        });
    }, observerOptions);

    // Observe all sections and feature items
    document.querySelectorAll('section, .feature-item, .hero-content').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
}

function initializeFormEnhancements() {
    // Premium form enhancements with loading states
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');
            if (submitBtn) {
                // Add loading state
                submitBtn.classList.add('loading');
                submitBtn.style.opacity = '0.7';
                submitBtn.disabled = true;
                
                // Simulate form submission (replace with actual form handling)
                setTimeout(() => {
                    submitBtn.classList.remove('loading');
                    submitBtn.style.opacity = '1';
                    submitBtn.disabled = false;
                    
                    // Show success message
                    showNotification('Form submitted successfully!', 'success');
                }, 2000);
            }
        });
    });
}

function initializeContactInteractions() {
    // Premium WhatsApp click handler with analytics
    const whatsappLink = document.querySelector('a[href*="wa.me"]');
    if (whatsappLink) {
        whatsappLink.addEventListener('click', function(e) {
            // Track WhatsApp clicks
            console.log('📱 WhatsApp clicked');
            
            // Add click animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    }

    // Premium phone number click handler
    const phoneNumbers = document.querySelectorAll('a[href^="tel:"], a[href*="647-884-3888"]');
    phoneNumbers.forEach(phone => {
        phone.addEventListener('click', function(e) {
            // Track phone clicks
            console.log('📞 Phone number clicked');
            
            // Add click animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

function initializeLazyLoading() {
    // Premium image lazy loading with intersection observer
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                img.classList.add('loaded');
                
                // Add fade-in animation
                img.style.opacity = '0';
                img.style.transform = 'scale(0.9)';
                
                setTimeout(() => {
                    img.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    img.style.opacity = '1';
                    img.style.transform = 'scale(1)';
                }, 100);
                
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        if (img.dataset.src) {
            imageObserver.observe(img);
        }
    });
}

function initializeBackToTop() {
    // Premium back to top button with smooth animation
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.className = 'back-to-top';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        background: var(--gradient-primary);
        color: white;
        border: none;
        border-radius: 50%;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 1000;
        box-shadow: 0 4px 20px rgba(236, 100, 36, 0.3);
        transform: translateY(20px);
    `;
    
    document.body.appendChild(backToTop);

    // Show/hide based on scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
            backToTop.style.visibility = 'visible';
            backToTop.style.transform = 'translateY(0)';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.visibility = 'hidden';
            backToTop.style.transform = 'translateY(20px)';
        }
    });

    // Smooth scroll to top
    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        
        // Add click animation
        backToTop.style.transform = 'scale(0.9)';
        setTimeout(() => {
            backToTop.style.transform = 'scale(1)';
        }, 150);
    });
}

function initializePerformanceOptimizations() {
    // Premium performance optimizations
    window.addEventListener('load', () => {
        // Remove loading states
        document.body.classList.add('loaded');
        
        // Preload critical images
        const criticalImages = [
            'extracted_website/Empire-Logo.png-1.jpeg',
            'extracted_website/Screen-Shot-2024-08-05-at-11.19.45-PM.png'
        ];
        
        criticalImages.forEach(src => {
            const img = new Image();
            img.src = src;
        });
        
        // Initialize service worker for caching (if needed)
        if ('serviceWorker' in navigator) {
            // Service worker registration can be added here
            console.log('🚀 Service Worker ready for caching');
        }
    });
}

function initializeHoverEffects() {
    // Premium hover effects with smooth transitions
    const buttons = document.querySelectorAll('.floorplan-button, a[href*="wa.me"], .feature-item');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
            this.style.boxShadow = '0 10px 30px rgba(0,0,0,0.2)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '';
        });
    });
    
    // Premium image hover effects
    const images = document.querySelectorAll('.feature-image img, .community-item img');
    images.forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.filter = 'brightness(1.1)';
        });
        
        img.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.filter = 'brightness(1)';
        });
    });
}

function showNotification(message, type = 'info') {
    // Premium notification system
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : '#2196F3'};
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Premium utility functions
function debounce(func, wait) {
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

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Premium scroll-based animations
const scrollHandler = throttle(() => {
    const scrolled = window.pageYOffset;
    const parallax = document.querySelector('.hero-background');
    
    if (parallax) {
        const speed = scrolled * 0.5;
        parallax.style.transform = `translateY(${speed}px)`;
    }
}, 16);

window.addEventListener('scroll', scrollHandler);

// Premium keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        // Close any open modals or overlays
        console.log('🔒 Escape pressed - closing overlays');
    }
});

// Premium touch gestures for mobile
let touchStartY = 0;
let touchEndY = 0;

document.addEventListener('touchstart', (e) => {
    touchStartY = e.changedTouches[0].screenY;
});

document.addEventListener('touchend', (e) => {
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartY - touchEndY;
    
    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe up
            console.log('👆 Swipe up detected');
        } else {
            // Swipe down
            console.log('👇 Swipe down detected');
        }
    }
} 