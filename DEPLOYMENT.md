# 🚀 Deployment Guide

## GitHub Pages Deployment

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New repository"
3. Name it: `empire-website` or `legacy-estates`
4. Make it **Public** (required for free GitHub Pages)
5. Don't initialize with README (we already have files)

### Step 2: Push to GitHub
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/empire-website.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" section
4. Under "Source", select "Deploy from a branch"
5. Select "main" branch
6. Click "Save"

### Step 4: Access Your Website
Your website will be available at:
```
https://YOUR_USERNAME.github.io/empire-website
```

## 🌐 Alternative Hosting Options

### Netlify (Free)
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop your `index.html` file
3. Get instant public URL

### Vercel (Free)
1. Go to [vercel.com](https://vercel.com)
2. Connect your GitHub repository
3. Auto-deploy on every push

## 📱 Current Local Access
- **Local**: `http://localhost:8000`
- **Same Network**: `http://172.20.10.12:8000`

## 🎯 Features Included
- ✅ HUGE Empire 30 logo
- ✅ Full-width responsive design
- ✅ All content sections
- ✅ Professional styling
- ✅ Interactive elements
- ✅ Mobile-friendly

## 🔧 Customization
- Edit `index.html` to change content
- Modify inline CSS for styling
- Add new images to `extracted_website/` folder 