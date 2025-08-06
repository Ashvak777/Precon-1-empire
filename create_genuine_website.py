import os
import shutil

def create_genuine_website():
    """Create a genuinely professional website with the best UI design"""
    
    print("🎨 Creating a genuinely professional website...")
    
    # Create the most professional HTML structure
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Homes | Legacy Estates in Thorold</title>
    <meta name="description" content="Premium Homes for Sale in Thorold, Heart of Niagara Region. Legacy Estates is Thorold's premier master-planned community featuring over 1,000 luxury townhomes and detached homes. Currently under construction at Kottmeier Road, Thorold.">
    <meta name="keywords" content="homes for sale thorold, new homes thorold, master planned community, niagara region homes, legacy estates">
    <link rel="icon" type="image/png" href="extracted_website/favicon.png">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="genuine_styles.css">
</head>
<body>
    <!-- Professional Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo-section">
                    <div class="logo">
                        <span class="logo-icon">L</span>
                        <span class="logo-text">LEGACYESTATES</span>
                    </div>
                </div>
                <div class="contact-info">
                    <p><a href="index.html">HOME</a> | T – 647-884-3888</p>
                </div>
            </div>
        </div>
    </header>

    <!-- Professional Black Banner -->
    <div class="black-banner">
        <div class="container">
            <h2>NEW RELEASE NOW ON SALE<br/>REGISTER TO LEARN MORE</h2>
        </div>
    </div>

    <!-- Hero Section with Professional Design -->
    <section class="hero">
        <div class="hero-background">
            <div class="hero-overlay">
                <div class="container">
                    <div class="hero-content">
                        <h1>LEGACY ESTATES</h1>
                        <div class="hero-subtitle">
                            <p>PREMIUM RELEASE OF<br/>TOWNS AND DETACHED</p>
                            <p>STARTING FROM $554,990</p>
                            <p>5% DEPOSIT</p>
                        </div>
                        <div class="hero-features">
                            <div class="feature-item">
                                <div class="feature-icon">🏠</div>
                                <div class="feature-text">Town's & Detached Homes</div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">📍</div>
                                <div class="feature-text">Thorold, ON</div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">📐</div>
                                <div class="feature-text">1,446 - 2,837 Sq. Ft.</div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">🛏️</div>
                                <div class="feature-text">3 - 4 Bedrooms</div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">🚿</div>
                                <div class="feature-text">2.5 - 3.5 Baths</div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">🏢</div>
                                <div class="feature-text">2 Storeys</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section with Professional Content -->
    <section class="about">
        <div class="container">
            <div class="about-content">
                <p>Legacy Estates is a premium master-planned community featuring over 1,000 luxury townhomes and detached homes in the prestigious city of Welland, located at Kottmeier Rd & Merritt Rd in the Niagara Region. This community offers residents convenient access to Downtown Welland, Port Colborne, the U.S. border, Lake Erie, and the attractions of Niagara Falls.</p>
                <p>Historically, investing in master-planned communities has yielded impressive returns. These developments not only introduce new homes but also new roads, infrastructure, and schools. We have personally invested in and sold hundreds of homes in previous Legacy master-planned communities, such as Imagine in Niagara Falls, Avalon in Caledonia, Lush & Victory in Hamilton, and Wyndfield in Brantford.</p>
            </div>
        </div>
    </section>

    <!-- Professional Contact Form Section -->
    <section class="contact-form">
        <div class="container">
            <div class="form-content">
                <h3>Get Price List & Floor Plans In Your Email</h3>
                <div class="form-container">
                    <script charset="utf-8" src="//js.hsforms.net/forms/embed/v2.js"></script>
                    <script>
                        hbspt.forms.create({
                            portalId: "23818724",
                            formId: "81a78d52-5303-49cf-914d-5a0936ee56de"
                        });
                    </script>
                </div>
                <div class="floorplan-section">
                    <img src="extracted_website/image1-6-1024x576-1.jpg.jpeg" alt="Legacy Estates Floorplans" class="floorplan-image">
                    <a href="index.html" class="floorplan-button">
                        Click here for Floorplans
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Legacy Estates Section -->
    <section class="why-legacy">
        <div class="container">
            <div class="section-header">
                <h2>Why Legacy Estates In Thorold?</h2>
            </div>
            
            <div class="features-grid">
                <!-- Master-Planned Community -->
                <div class="feature-item">
                    <div class="feature-image">
                        <img src="extracted_website/64867764-0-Empire-Legacy-2-St.png" alt="Master-Planned Community">
                    </div>
                    <div class="feature-content">
                        <h3>Master-Planned Community</h3>
                        <p>Master-planned developments are ideal for both investors and residents, offering a brand-new community with updated roads, infrastructure, schools, and more. Legacy has successfully built these communities throughout Southern Ontario. Those who invested early in these projects have seen remarkable returns.</p>
                    </div>
                </div>

                <!-- Tourist Hotspot -->
                <div class="feature-item">
                    <div class="feature-content">
                        <h3>Tourist Hotspot</h3>
                        <p>Niagara Falls attracts over 13 million visitors annually and supports 40,000 jobs in the thriving tourism sector. The region is rich in amenities, featuring over 150 hotels and motels, more than 90 wineries, over 40 golf courses, and two casinos. With annual spending exceeding $2.4 billion, the local real estate market is strongly supported.</p>
                    </div>
                    <div class="feature-image">
                        <img src="extracted_website/img05.jpg.jpeg" alt="New Homes at Legacy Canal">
                    </div>
                </div>

                <!-- Population Growth -->
                <div class="feature-item">
                    <div class="feature-image">
                        <img src="extracted_website/64867768-0-Empire-Legacy-38-D.png" alt="Population Growth">
                    </div>
                    <div class="feature-content">
                        <h3>Population Growth</h3>
                        <p>The population of the Niagara Region is projected to grow by 28%, reaching 610,000 people by 2041. This population increase will drive housing demand, promising substantial returns for current investors.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Company Info Section -->
    <section class="company-info">
        <div class="container">
            <div class="company-content">
                <div class="company-logo">
                    <div class="logo-large">
                        <span class="logo-icon-large">L</span>
                        <span class="logo-text-large">LEGACY 30</span>
                    </div>
                </div>
                <div class="company-description">
                    <p>With over 30 years of experience, Legacy Communities is one of the country's largest developers, having constructed over 15,000 homes and condos across the GTA and Southwestern Ontario. Their commitment to excellence, innovation, and vibrant community building is evident in the glowing reviews and testimonials from residents. Dedicated to sustainable building practices and seamless community integration, Legacy has received prestigious awards, including the double Cross Border Builder Challenge award, highlighting their relentless pursuit of excellence in the real estate sector.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Map Section -->
    <section class="map-section">
        <div class="container">
            <div class="map-container">
                <iframe allowfullscreen height="450" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d11664.310942750366!2d-79.2282811!3d43.0397959!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d348c3cd21086d%3A0x9fe5d5bcd6bee1f2!2sLegacy%20Estates%20%7C%20Legacy%20Communities!5e0!3m2!1sen!2sca!4v1711344471142!5m2!1sen!2sca" style="border: 0;" width="600"></iframe>
            </div>
            <div class="contact-highlight">
                <h4>PREMIUM RELEASE OF HOMES NOW ON SALE<br/>By Appointment Only!</h4>
                <h3>-> 647-884-3888 <-</h3>
            </div>
        </div>
    </section>

    <!-- Nearby Communities Section -->
    <section class="nearby-communities">
        <div class="container">
            <div class="section-header">
                <h2>—> COMMUNITIES NEARBY LEGACY <—</h2>
            </div>
            <div class="communities-grid">
                <div class="community-item">
                    <a href="http://WWW.LEGACYCANALS.CA" target="_blank">
                        <img src="extracted_website/Screen-Shot-2024-08-05-at-11.27.07-PM.png" alt="Legacy Canals">
                    </a>
                </div>
                <div class="community-item">
                    <a href="http://WWW.WYNDFIELDLEGACY.COM" target="_blank">
                        <img src="extracted_website/Screen-Shot-2024-08-05-at-11.28.31-PM.png" alt="Wyndfield Legacy">
                    </a>
                </div>
                <div class="community-item">
                    <img src="extracted_website/Screen-Shot-2024-08-05-at-11.30.39-PM.png" alt="Legacy Communities">
                </div>
            </div>
        </div>
    </section>

    <!-- Registration Section -->
    <section class="registration">
        <div class="container">
            <div class="registration-content">
                <div class="form-container">
                    <script charset="utf-8" src="//js.hsforms.net/forms/embed/v2.js"></script>
                    <script>
                        hbspt.forms.create({
                            portalId: "23818724",
                            formId: "81a78d52-5303-49cf-914d-5a0936ee56de"
                        });
                    </script>
                </div>
                <div class="disclaimer">
                    <h6>We do not represent the builder. We are not affiliated with the builder. Any unauthorized use of Legacy Communities' trademarks is prohibited. All renderings are artist concepts. Floor plans, incentives, pricing are subject to terms & conditions and may change at any time without notice – see sales representatives for more details. E&OE</h6>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-info">
                    <img src="extracted_website/favicon.png" alt="Legacy Estates" class="contact-logo">
                    <p class="contact-phone">Direct line – 647-884-3888 (Clients Only)</p>
                    <p class="terms">*Terms & Conditions Apply – See Sales Representative For More Information</p>
                    <p class="disclaimer-text">We are not the builder's representatives or affiliated with them. Unauthorized use of Legacy Communities' trademarks is prohibited. Renderings are artist concepts, and floor plans, incentives, and pricing are subject to terms and conditions, and may change without notice. For more details, consult sales representatives. Errors and omissions excepted (E&OE).</p>
                </div>
                <div class="whatsapp-section">
                    <a href="https://wa.me/16478843888" target="_blank">
                        <img src="extracted_website/whatsapp-chat-link-black-1-1.png" alt="WhatsApp Contact">
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Professional Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p class="copyright">2024© All Rights Reserved.</p>
                <p class="disclaimer">*WE DO NOT REPRESENT THE BUILDER*</p>
            </div>
        </div>
    </footer>

    <script src="genuine_script.js"></script>
</body>
</html>'''
    
    # Create professional CSS
    css_content = '''/* Professional Genuine Website Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #ffffff;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Professional Header */
.header {
    background: #ffffff;
    padding: 15px 0;
    border-bottom: 1px solid #e5e5e5;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
}

.logo-icon {
    background: #ec6424;
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
}

.logo-text {
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    letter-spacing: 1px;
}

.contact-info p {
    font-size: 14px;
    color: #666;
}

.contact-info a {
    color: #ec6424;
    text-decoration: none;
    font-weight: 600;
}

/* Professional Black Banner */
.black-banner {
    background: linear-gradient(135deg, #1a1a1a 0%, #2c2c2c 100%);
    padding: 20px 0;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.black-banner h2 {
    color: #ffffff;
    font-size: 20px;
    font-weight: 600;
    margin: 0;
    line-height: 1.4;
    letter-spacing: 1px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

/* Hero Section */
.hero {
    position: relative;
    height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('extracted_website/Screen-Shot-2024-08-05-at-11.19.45-PM.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(236, 100, 36, 0.9) 0%, rgba(236, 100, 36, 0.8) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-content {
    position: relative;
    z-index: 2;
    color: #ffffff;
    max-width: 800px;
}

.hero-content h1 {
    font-size: 56px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 30px;
    letter-spacing: 3px;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    line-height: 1.1;
}

.hero-subtitle p {
    font-size: 28px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 15px;
    line-height: 1.3;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);
}

.hero-features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.feature-item {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.feature-icon {
    font-size: 24px;
    margin-bottom: 8px;
}

.feature-text {
    font-size: 12px;
    font-weight: 500;
    color: #ffffff;
    line-height: 1.3;
}

/* About Section */
.about {
    padding: 80px 0;
    background: #f8f9fa;
}

.about-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.about-content p {
    font-size: 18px;
    line-height: 1.8;
    margin-bottom: 25px;
    color: #555;
}

/* Contact Form Section */
.contact-form {
    padding: 80px 0;
    background: #ffffff;
}

.form-content {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.form-content h3 {
    font-size: 32px;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 30px;
}

.form-container {
    margin-bottom: 40px;
}

.floorplan-section {
    text-align: center;
}

.floorplan-image {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    margin-bottom: 30px;
}

.floorplan-button {
    background: linear-gradient(135deg, #ec6424 0%, #d63384 100%);
    color: white;
    padding: 18px 36px;
    text-decoration: none;
    border-radius: 50px;
    font-weight: 600;
    font-size: 16px;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(236, 100, 36, 0.3);
}

.floorplan-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(236, 100, 36, 0.4);
}

/* Why Legacy Section */
.why-legacy {
    padding: 80px 0;
    background: linear-gradient(135deg, #ec6424 0%, #d63384 100%);
    color: white;
}

.section-header {
    text-align: center;
    margin-bottom: 60px;
}

.section-header h2 {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 20px;
}

.features-grid {
    display: grid;
    gap: 60px;
}

.feature-item {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
}

.feature-item:nth-child(even) {
    direction: rtl;
}

.feature-item:nth-child(even) .feature-content {
    direction: ltr;
}

.feature-image img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

.feature-content h3 {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: white;
}

.feature-content p {
    font-size: 16px;
    line-height: 1.8;
    color: rgba(255, 255, 255, 0.9);
}

/* Company Info Section */
.company-info {
    padding: 80px 0;
    background: #f8f9fa;
}

.company-content {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.logo-large {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-bottom: 40px;
}

.logo-icon-large {
    background: #ec6424;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 28px;
}

.logo-text-large {
    font-size: 36px;
    font-weight: 800;
    color: #2c3e50;
    letter-spacing: 2px;
}

.company-description p {
    font-size: 18px;
    line-height: 1.8;
    color: #555;
}

/* Map Section */
.map-section {
    padding: 80px 0;
    background: #ffffff;
}

.map-container {
    margin-bottom: 40px;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.contact-highlight {
    text-align: center;
    background: linear-gradient(135deg, #ec6424 0%, #d63384 100%);
    padding: 30px;
    border-radius: 12px;
    color: white;
}

.contact-highlight h4 {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 15px;
}

.contact-highlight h3 {
    font-size: 28px;
    font-weight: 800;
}

/* Nearby Communities */
.nearby-communities {
    padding: 80px 0;
    background: #f8f9fa;
}

.communities-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
}

.community-item img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.community-item img:hover {
    transform: translateY(-5px);
}

/* Registration Section */
.registration {
    padding: 80px 0;
    background: #ffffff;
}

.registration-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.disclaimer h6 {
    font-size: 14px;
    line-height: 1.6;
    color: #666;
    margin-top: 40px;
}

/* Contact Section */
.contact {
    padding: 80px 0;
    background: #f8f9fa;
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
}

.contact-info {
    text-align: center;
}

.contact-logo {
    width: 80px;
    height: auto;
    margin-bottom: 20px;
}

.contact-phone {
    font-size: 18px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 15px;
}

.terms, .disclaimer-text {
    font-size: 12px;
    color: #666;
    line-height: 1.5;
    margin-bottom: 10px;
}

.whatsapp-section img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    transition: transform 0.3s ease;
}

.whatsapp-section img:hover {
    transform: scale(1.02);
}

/* Footer */
.footer {
    background: #2c3e50;
    color: white;
    padding: 30px 0;
    text-align: center;
}

.footer-content p {
    margin-bottom: 10px;
    font-size: 14px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 40px;
    }
    
    .hero-subtitle p {
        font-size: 20px;
    }
    
    .hero-features {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .feature-item {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .feature-item:nth-child(even) {
        direction: ltr;
    }
    
    .communities-grid {
        grid-template-columns: 1fr;
    }
    
    .contact-content {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .logo-text {
        font-size: 18px;
    }
    
    .logo-text-large {
        font-size: 28px;
    }
}

@media (max-width: 480px) {
    .hero-features {
        grid-template-columns: 1fr;
    }
    
    .hero-content h1 {
        font-size: 32px;
    }
    
    .hero-subtitle p {
        font-size: 16px;
    }
}'''

    # Create professional JavaScript
    js_content = '''// Professional Genuine Website JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling for all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Header scroll effect
    const header = document.querySelector('.header');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > lastScroll && currentScroll > 100) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all sections for animation
    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });

    // Form enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');
            if (submitBtn) {
                submitBtn.style.opacity = '0.7';
                submitBtn.disabled = true;
            }
        });
    });

    // WhatsApp click handler
    const whatsappLink = document.querySelector('a[href*="wa.me"]');
    if (whatsappLink) {
        whatsappLink.addEventListener('click', function(e) {
            // Track WhatsApp clicks
            console.log('WhatsApp clicked');
        });
    }

    // Phone number click handler
    const phoneNumbers = document.querySelectorAll('a[href^="tel:"], a[href*="647-884-3888"]');
    phoneNumbers.forEach(phone => {
        phone.addEventListener('click', function(e) {
            // Track phone clicks
            console.log('Phone number clicked');
        });
    });

    // Image lazy loading
    const images = document.querySelectorAll('img');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        if (img.dataset.src) {
            imageObserver.observe(img);
        }
    });

    // Back to top button
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.className = 'back-to-top';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: #ec6424;
        color: white;
        border: none;
        border-radius: 50%;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 15px rgba(236, 100, 36, 0.3);
    `;
    
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
        } else {
            backToTop.style.opacity = '0';
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Performance optimization
    window.addEventListener('load', () => {
        // Remove loading states
        document.body.classList.add('loaded');
    });

    // Professional hover effects
    const buttons = document.querySelectorAll('.floorplan-button, a[href*="wa.me"]');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    console.log('Legacy Estates website loaded successfully');
});'''

    # Save all files
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    with open('genuine_styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    with open('genuine_script.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("✅ Genuine professional website created!")
    print("🎨 Features:")
    print("   - Professional modern design")
    print("   - Smooth animations and transitions")
    print("   - Responsive layout")
    print("   - Interactive elements")
    print("   - Professional typography")
    print("   - Authentic branding")
    print("   - High-quality user experience")
    
    return True

if __name__ == "__main__":
    create_genuine_website() 