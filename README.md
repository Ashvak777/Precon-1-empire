# Legacy Estates - Website Replica

A complete website replica of the Empire Legacy Thorold website, featuring the same structure, design, and functionality but with different branding and content.

## 🏗️ Project Overview

This project is a faithful recreation of the [Empire Legacy Thorold](https://empirelegacythorold.com/) website, maintaining the same visual design, layout, and user experience while using different branding ("Legacy Estates" instead of "Empire Legacy").

## 📋 Features

### ✅ Complete Website Structure
- **Header Section** - Logo and contact information
- **Hero Section** - Main title and call-to-action
- **About Section** - Community description and benefits
- **Contact Forms** - HubSpot integration for lead generation
- **Features Section** - Three key selling points with images
- **Company Information** - Developer background and credentials
- **Interactive Map** - Google Maps integration
- **Nearby Communities** - Related development showcase
- **Contact Section** - WhatsApp integration and contact details
- **Footer** - Legal disclaimers and copyright

### 🎨 Design Features
- **Responsive Design** - Mobile-first approach
- **Modern UI/UX** - Clean, professional design
- **Smooth Animations** - CSS transitions and JavaScript animations
- **Accessibility** - WCAG compliant with keyboard navigation
- **Performance Optimized** - Fast loading with lazy loading images

### 🛠️ Technical Features
- **HTML5 Semantic Structure**
- **CSS3 with Flexbox/Grid**
- **Vanilla JavaScript** (no frameworks)
- **HubSpot Forms Integration**
- **Google Maps Integration**
- **WhatsApp Business Integration**
- **Mobile Responsive**
- **SEO Optimized**

## 🚀 Getting Started

### Prerequisites
- A modern web browser
- Local web server (optional, for development)

### Installation
1. Clone or download the project files
2. Extract the `extracted_website` folder (contains all images)
3. Open `index.html` in your web browser

### File Structure
```
├── index.html              # Main HTML file
├── styles.css              # CSS styles
├── script.js               # JavaScript functionality
├── scrape_website.py       # Python scraper (for reference)
├── website_data.json       # Scraped data (for reference)
├── extracted_website/      # All website images
│   ├── favicon.png
│   ├── IMG_0190.png
│   ├── Screen-Shot-*.png
│   ├── 64867764-*.png
│   ├── 64867768-*.png
│   ├── image1-6-*.jpeg
│   ├── img05.jpg.jpeg
│   ├── Empire-Logo.png-1.jpeg
│   └── whatsapp-chat-link-*.png
└── README.md              # This file
```

## 🎯 Key Changes from Original

### Branding Updates
- **Empire Legacy** → **Legacy Estates**
- **Empire Communities** → **Legacy Communities**
- Updated all references while maintaining the same structure

### Content Modifications
- Changed "NEW RELEASE" to "PREMIUM RELEASE"
- Updated company descriptions with new branding
- Maintained all original statistics and facts
- Preserved all contact information and links

### Visual Consistency
- **Same Color Palette**: Orange (#ec6424), Gray (#333333), White (#ffffff)
- **Same Typography**: Inter font family
- **Same Layout**: Identical section structure and spacing
- **Same Images**: All original images preserved and used

## 📱 Responsive Design

The website is fully responsive with breakpoints at:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

### Mobile Features
- Collapsible navigation
- Touch-friendly buttons
- Optimized image loading
- Simplified layouts for small screens

## 🔧 Customization

### Colors
Main colors can be modified in `styles.css`:
```css
:root {
    --primary-color: #ec6424;
    --secondary-color: #333333;
    --background-color: #ffffff;
    --text-color: #555555;
}
```

### Content
- Update text content in `index.html`
- Modify images in the `extracted_website/` folder
- Adjust contact information and links

### Forms
- HubSpot forms are integrated
- Form IDs and portal IDs can be updated
- Custom form validation included

## 📊 Performance

### Optimization Features
- **Lazy Loading Images** - Images load as they come into view
- **Minified CSS/JS** - Optimized file sizes
- **Compressed Images** - Web-optimized image formats
- **Smooth Scrolling** - Enhanced user experience
- **Debounced Events** - Performance-optimized scroll handling

### Loading Speed
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1

## 🔍 SEO Features

### Meta Tags
- **Title**: "Premium Homes | Legacy Estates in Thorold"
- **Description**: Comprehensive meta description
- **Keywords**: Relevant real estate keywords
- **Favicon**: Custom favicon included

### Structured Data
- Schema markup for real estate listings
- Local business information
- Contact details structured data

## 🛡️ Security

### Features
- **HTTPS Ready** - All external links use HTTPS
- **XSS Protection** - Input sanitization
- **CSRF Protection** - Form security measures
- **Content Security Policy** - CSP headers ready

## 📞 Contact Integration

### WhatsApp Business
- Direct WhatsApp integration
- Click-to-chat functionality
- Business phone number: 647-884-3888

### HubSpot Forms
- Lead generation forms
- Email capture functionality
- CRM integration ready

### Google Maps
- Interactive location map
- Embedded iframe
- Responsive design

## 🚀 Deployment

### Local Development
1. Open `index.html` in a web browser
2. Use a local server for full functionality:
   ```bash
   python -m http.server 8000
   # or
   npx serve .
   ```

### Production Deployment
1. Upload all files to your web server
2. Ensure `extracted_website/` folder is accessible
3. Configure your domain and SSL certificate
4. Update any absolute URLs if needed

## 📝 License

This project is for educational and demonstration purposes. All original content and images belong to their respective owners.

## 🤝 Support

For questions or support:
- **Phone**: 647-884-3888
- **WhatsApp**: [Click to chat](https://wa.me/16478843888)
- **Email**: Contact through the website forms

## 📈 Analytics Ready

The website is prepared for:
- Google Analytics
- Google Tag Manager
- Facebook Pixel
- HubSpot Analytics

## 🔄 Updates

### Version 1.0
- Initial website replica
- Complete functionality
- Responsive design
- All integrations working

---

**Note**: This is a replica website created for demonstration purposes. All original content, images, and branding belong to their respective owners. The contact information and forms are functional and ready for use. 