import requests
from bs4 import BeautifulSoup
import json
import os
import re
from urllib.parse import urljoin, urlparse
import time
import subprocess
import shutil

def clone_website_exact(url, output_dir="exact_clone"):
    """Clone the website exactly as it appears"""
    
    print("🔍 Starting exact website clone...")
    
    # Create output directory
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Get the main page
        print("📥 Fetching main page...")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all CSS
        print("🎨 Extracting CSS...")
        css_files = []
        
        # Inline styles
        inline_styles = soup.find_all('style')
        for i, style in enumerate(inline_styles):
            css_content = style.string
            if css_content:
                filename = f"inline_style_{i}.css"
                with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                    f.write(css_content)
                css_files.append(filename)
        
        # External CSS files
        css_links = soup.find_all('link', rel='stylesheet')
        for i, link in enumerate(css_links):
            css_url = urljoin(url, link.get('href', ''))
            try:
                css_response = requests.get(css_url, headers=headers, timeout=10)
                if css_response.status_code == 200:
                    filename = f"external_style_{i}.css"
                    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                        f.write(css_response.text)
                    css_files.append(filename)
                    print(f"✅ Downloaded: {css_url}")
            except Exception as e:
                print(f"❌ Failed to download CSS: {css_url} - {e}")
        
        # Extract all JavaScript
        print("⚡ Extracting JavaScript...")
        js_files = []
        
        # Inline scripts
        inline_scripts = soup.find_all('script')
        for i, script in enumerate(inline_scripts):
            if script.string:
                filename = f"inline_script_{i}.js"
                with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                    f.write(script.string)
                js_files.append(filename)
        
        # External JavaScript files
        script_tags = soup.find_all('script', src=True)
        for i, script in enumerate(script_tags):
            js_url = urljoin(url, script.get('src', ''))
            try:
                js_response = requests.get(js_url, headers=headers, timeout=10)
                if js_response.status_code == 200:
                    filename = f"external_script_{i}.js"
                    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                        f.write(js_response.text)
                    js_files.append(filename)
                    print(f"✅ Downloaded: {js_url}")
            except Exception as e:
                print(f"❌ Failed to download JS: {js_url} - {e}")
        
        # Download all images
        print("🖼️ Downloading images...")
        images = soup.find_all('img')
        image_files = []
        
        for i, img in enumerate(images):
            img_src = img.get('src', '')
            if img_src:
                img_url = urljoin(url, img_src)
                try:
                    img_response = requests.get(img_url, headers=headers, timeout=10)
                    if img_response.status_code == 200:
                        # Extract file extension
                        parsed_url = urlparse(img_url)
                        filename = f"image_{i}{os.path.splitext(parsed_url.path)[1]}"
                        if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                            filename += '.jpg'
                        
                        with open(os.path.join(output_dir, filename), 'wb') as f:
                            f.write(img_response.content)
                        image_files.append(filename)
                        print(f"✅ Downloaded: {img_url}")
                except Exception as e:
                    print(f"❌ Failed to download image: {img_url} - {e}")
        
        # Create the exact HTML clone
        print("📄 Creating exact HTML clone...")
        
        # Replace external CSS links with local files
        for i, link in enumerate(css_links):
            if i < len(css_files):
                link['href'] = css_files[i]
        
        # Replace external JS links with local files
        for i, script in enumerate(script_tags):
            if i < len(js_files):
                script['src'] = js_files[i]
        
        # Replace image sources with local files
        for i, img in enumerate(images):
            if i < len(image_files):
                img['src'] = image_files[i]
        
        # Save the exact HTML
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"✅ Exact clone created in: {output_dir}")
        print(f"📊 Summary:")
        print(f"   - CSS files: {len(css_files)}")
        print(f"   - JS files: {len(js_files)}")
        print(f"   - Images: {len(image_files)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error cloning website: {e}")
        return False

def create_exact_replica():
    """Create an exact replica using the extracted images and structure"""
    
    print("🎯 Creating exact replica with different branding...")
    
    # Use the existing extracted images
    image_dir = "extracted_website"
    
    # Create the exact HTML structure
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Homes | Legacy Estates in Thorold</title>
    <meta name="description" content="Premium Homes for Sale in Thorold, Heart of Niagara Region. Legacy Estates is Thorold's premier master-planned community featuring over 1,000 luxury townhomes and detached homes. Currently under construction at Kottmeier Road, Thorold.">
    <meta name="keywords" content="homes for sale thorold, new homes thorold, master planned community, niagara region homes, legacy estates">
    <link rel="icon" type="image/png" href="extracted_website/favicon.png">
    <link rel="stylesheet" href="exact_styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Black Banner -->
    <div class="black-banner">
        <div class="container">
            <h2>NEW RELEASE NOW ON SALE<br/>REGISTER TO LEARN MORE</h2>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo-section">
                    <a href="https://empirecanals.ca/" target="_blank">
                        <img src="extracted_website/IMG_0190.png" alt="Legacy Estates Logo" class="logo">
                    </a>
                </div>
                <div class="contact-info">
                    <p><a href="index.html">HOME</a> | T – 647-884-3888</p>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
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
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about">
        <div class="container">
            <div class="about-content">
                <p>Legacy Estates is a highly desirable master-planned community featuring over 1,000 new luxury townhomes and detached homes in the scenic city of Welland, located at Kottmeier Rd & Merritt Rd in the Niagara Region. This community offers residents convenient access to Downtown Welland, Port Colborne, the U.S. border, Lake Erie, and the attractions of Niagara Falls.</p>
                <p>Historically, investing in master-planned communities has yielded impressive returns. These developments not only introduce new homes but also new roads, infrastructure, and schools. We have personally invested in and sold hundreds of homes in previous Legacy master-planned communities, such as Imagine in Niagara Falls, Avalon in Caledonia, Lush & Victory in Hamilton, and Wyndfield in Brantford.</p>
            </div>
        </div>
    </section>

    <!-- Contact Form Section -->
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
                    <img src="extracted_website/Empire-Logo.png-1.jpeg" alt="Legacy Communities Logo">
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
                <iframe allowfullscreen height="450" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d11664.310942750366!2d-79.2282811!3d43.0397959!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d348c3cd21086d%3A0x9fe5d5bcd6bee1f2!2sEmpire%20Legacy%20%7C%20Empire%20Communities!5e0!3m2!1sen!2sca!4v1711344471142!5m2!1sen!2sca" style="border: 0;" width="600"></iframe>
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
                    <a href="http://WWW.EMPIRECANALS.CA" target="_blank">
                        <img src="extracted_website/Screen-Shot-2024-08-05-at-11.27.07-PM.png" alt="Legacy Canals">
                    </a>
                </div>
                <div class="community-item">
                    <a href="http://WWW.WYNDFIELDEMPIRE.COM" target="_blank">
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

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <p class="copyright">2024© All Rights Reserved.</p>
                <p class="disclaimer">*WE DO NOT REPRESENT THE BUILDER*</p>
            </div>
        </div>
    </footer>

    <script src="exact_script.js"></script>
</body>
</html>'''
    
    # Save the exact HTML
    with open('exact_index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Exact replica HTML created: exact_index.html")
    return True

if __name__ == "__main__":
    print("🚀 Starting exact website cloning process...")
    
    # First, try to clone the exact website
    success = clone_website_exact("https://empirelegacythorold.com/")
    
    if success:
        print("✅ Exact clone completed!")
    else:
        print("⚠️ Exact clone failed, creating replica with extracted images...")
        create_exact_replica()
    
    print("🎯 Process completed!") 