import requests
from bs4 import BeautifulSoup
import json
import os
import re
from urllib.parse import urljoin, urlparse
import time

def scrape_website(url):
    """Scrape the website and extract all information"""
    
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
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all information
        website_data = {
            'url': url,
            'title': soup.title.string if soup.title else '',
            'meta_description': '',
            'meta_keywords': '',
            'favicon': '',
            'content': {},
            'styles': {},
            'images': [],
            'links': [],
            'scripts': [],
            'colors': [],
            'fonts': []
        }
        
        # Extract meta tags
        meta_tags = soup.find_all('meta')
        for meta in meta_tags:
            if meta.get('name') == 'description':
                website_data['meta_description'] = meta.get('content', '')
            elif meta.get('name') == 'keywords':
                website_data['meta_keywords'] = meta.get('content', '')
        
        # Extract favicon
        favicon = soup.find('link', rel='icon') or soup.find('link', rel='shortcut icon')
        if favicon:
            website_data['favicon'] = urljoin(url, favicon.get('href', ''))
        
        # Extract all text content by sections
        sections = {}
        
        # Header section
        header = soup.find('header') or soup.find('nav')
        if header:
            sections['header'] = {
                'text': header.get_text(strip=True),
                'html': str(header)
            }
        
        # Main content
        main = soup.find('main') or soup.find('body')
        if main:
            sections['main'] = {
                'text': main.get_text(strip=True),
                'html': str(main)
            }
        
        # Footer
        footer = soup.find('footer')
        if footer:
            sections['footer'] = {
                'text': footer.get_text(strip=True),
                'html': str(footer)
            }
        
        # Extract all headings
        headings = {}
        for i in range(1, 7):
            h_tags = soup.find_all(f'h{i}')
            if h_tags:
                headings[f'h{i}'] = [tag.get_text(strip=True) for tag in h_tags]
        
        sections['headings'] = headings
        
        # Extract all paragraphs
        paragraphs = soup.find_all('p')
        sections['paragraphs'] = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
        
        # Extract all links
        links = soup.find_all('a')
        sections['links'] = []
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if href and text:
                sections['links'].append({
                    'text': text,
                    'href': urljoin(url, href)
                })
        
        # Extract all images
        images = soup.find_all('img')
        sections['images'] = []
        for img in images:
            src = img.get('src', '')
            alt = img.get('alt', '')
            if src:
                sections['images'].append({
                    'src': urljoin(url, src),
                    'alt': alt,
                    'title': img.get('title', '')
                })
        
        # Extract all buttons
        buttons = soup.find_all('button')
        sections['buttons'] = []
        for button in buttons:
            sections['buttons'].append({
                'text': button.get_text(strip=True),
                'class': button.get('class', []),
                'id': button.get('id', '')
            })
        
        # Extract all forms
        forms = soup.find_all('form')
        sections['forms'] = []
        for form in forms:
            form_data = {
                'action': form.get('action', ''),
                'method': form.get('method', ''),
                'inputs': []
            }
            inputs = form.find_all('input')
            for inp in inputs:
                form_data['inputs'].append({
                    'type': inp.get('type', ''),
                    'name': inp.get('name', ''),
                    'placeholder': inp.get('placeholder', ''),
                    'value': inp.get('value', '')
                })
            sections['forms'].append(form_data)
        
        website_data['content'] = sections
        
        # Extract CSS styles
        styles = soup.find_all('style')
        website_data['styles']['inline'] = [style.string for style in styles if style.string]
        
        # Extract external CSS links
        css_links = soup.find_all('link', rel='stylesheet')
        website_data['styles']['external'] = [urljoin(url, link.get('href', '')) for link in css_links]
        
        # Extract JavaScript
        scripts = soup.find_all('script')
        website_data['scripts'] = []
        for script in scripts:
            if script.string:
                website_data['scripts'].append({
                    'type': 'inline',
                    'content': script.string
                })
            elif script.get('src'):
                website_data['scripts'].append({
                    'type': 'external',
                    'src': urljoin(url, script.get('src', ''))
                })
        
        # Extract colors (basic extraction from inline styles)
        color_pattern = r'#[0-9a-fA-F]{3,6}|rgb\([^)]+\)|rgba\([^)]+\)'
        all_styles = ' '.join(website_data['styles']['inline'])
        colors = re.findall(color_pattern, all_styles)
        website_data['colors'] = list(set(colors))
        
        # Extract fonts (basic extraction)
        font_pattern = r'font-family:\s*([^;]+)'
        fonts = re.findall(font_pattern, all_styles)
        website_data['fonts'] = list(set(fonts))
        
        return website_data
        
    except Exception as e:
        print(f"Error scraping website: {e}")
        return None

def save_website_data(data, filename='website_data.json'):
    """Save the scraped data to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Website data saved to {filename}")

def extract_page_sections(data):
    """Extract different page sections from the scraped data"""
    if not data or 'content' not in data:
        return {}
    
    sections = {}
    content = data['content']
    
    # Extract main sections
    if 'main' in content:
        main_html = content['main']['html']
        soup = BeautifulSoup(main_html, 'html.parser')
        
        # Look for common section patterns
        section_selectors = [
            'section',
            '.section',
            '.hero',
            '.banner',
            '.content',
            '.main-content',
            '.sidebar',
            '.footer'
        ]
        
        for selector in section_selectors:
            elements = soup.select(selector)
            if elements:
                sections[selector] = []
                for element in elements:
                    sections[selector].append({
                        'text': element.get_text(strip=True),
                        'html': str(element)
                    })
    
    return sections

if __name__ == "__main__":
    url = "https://empirelegacythorold.com/"
    
    print("Scraping website...")
    website_data = scrape_website(url)
    
    if website_data:
        print("Website scraped successfully!")
        print(f"Title: {website_data['title']}")
        print(f"Meta Description: {website_data['meta_description']}")
        print(f"Number of images: {len(website_data['content'].get('images', []))}")
        print(f"Number of links: {len(website_data['content'].get('links', []))}")
        
        # Save the data
        save_website_data(website_data)
        
        # Extract sections
        sections = extract_page_sections(website_data)
        print(f"Found {len(sections)} main sections")
        
        # Print some key information
        if 'headings' in website_data['content']:
            print("\nHeadings found:")
            for level, headings in website_data['content']['headings'].items():
                print(f"{level}: {headings}")
        
        if 'paragraphs' in website_data['content']:
            print(f"\nNumber of paragraphs: {len(website_data['content']['paragraphs'])}")
            for i, para in enumerate(website_data['content']['paragraphs'][:5]):  # Show first 5
                print(f"Paragraph {i+1}: {para[:100]}...")
        
    else:
        print("Failed to scrape website") 