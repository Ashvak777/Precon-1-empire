import os
import shutil
import re

def create_perfect_clone():
    """Create a perfect clone with Legacy Estates branding"""
    
    print("🎯 Creating perfect clone with Legacy Estates branding...")
    
    # Read the exact clone HTML
    with open('exact_clone/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Replace all branding from Empire Legacy to Legacy Estates
    replacements = {
        # Title and meta descriptions
        'Homes For Sale | Empire Legacy in Thorold': 'Premium Homes | Legacy Estates in Thorold',
        'Empire Legacy': 'Legacy Estates',
        'Empire Communities': 'Legacy Communities',
        'Empire Canals': 'Legacy Canals',
        
        # Content replacements
        'Empire Legacy is Thorold\'s first master-planned community': 'Legacy Estates is Thorold\'s premier master-planned community',
        'Empire Legacy is a new townhouse and single family home development By Empire Communities': 'Legacy Estates is a luxury townhouse and single family home development By Legacy Communities',
        
        # Phone and contact info (keep the same)
        '647-884-3888': '647-884-3888',
        
        # Links and references
        'empirecanals.ca': 'legacycanals.ca',
        'WWW.EMPIRECANALS.CA': 'WWW.LEGACYCANALS.CA',
        'WWW.WYNDFIELDEMPIRE.COM': 'WWW.WYNDFIELDLEGACY.COM',
        
        # Form and script references (keep the same for functionality)
        'portalId: "23818724"': 'portalId: "23818724"',
        'formId: "81a78d52-5303-49cf-914d-5a0936ee56de"': 'formId: "81a78d52-5303-49cf-914d-5a0936ee56de"',
        
        # Map and location references
        'Empire%20Legacy%20%7C%20Empire%20Communities': 'Legacy%20Estates%20%7C%20Legacy%20Communities',
        
        # Disclaimer text
        'Empire Communities\' trademarks': 'Legacy Communities\' trademarks',
        'Unauthorized use of Empire Communities\' trademarks': 'Unauthorized use of Legacy Communities\' trademarks',
    }
    
    # Apply all replacements
    for old_text, new_text in replacements.items():
        html_content = html_content.replace(old_text, new_text)
    
    # Additional content improvements
    content_improvements = {
        'highly desirable master-planned community': 'premium master-planned community',
        'over 1,000 new townhomes and detached homes': 'over 1,000 luxury townhomes and detached homes',
        'scenic city of Welland': 'prestigious city of Welland',
        'We have personally invested in and sold hundreds of homes in previous Empire master-planned communities': 'We have personally invested in and sold hundreds of homes in previous Legacy master-planned communities',
        'Empire has successfully built these communities': 'Legacy has successfully built these communities',
        'Empire has received prestigious awards': 'Legacy has received prestigious awards',
        'Empire\'s relentless pursuit of excellence': 'Legacy\'s relentless pursuit of excellence',
    }
    
    for old_text, new_text in content_improvements.items():
        html_content = html_content.replace(old_text, new_text)
    
    # Save the perfect clone
    with open('perfect_clone.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Copy all assets to current directory
    print("📁 Copying all assets...")
    for file in os.listdir('exact_clone'):
        if file != 'index.html':
            src = os.path.join('exact_clone', file)
            dst = os.path.join('.', file)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"✅ Copied: {file}")
    
    print("✅ Perfect clone created: perfect_clone.html")
    return True

def serve_perfect_clone():
    """Serve the perfect clone"""
    
    print("🚀 Starting server for perfect clone...")
    print("📱 Open your browser and go to: http://localhost:8000/perfect_clone.html")
    
    # Start the server
    os.system("python3 -m http.server 8000")

if __name__ == "__main__":
    create_perfect_clone()
    print("\n🎯 Perfect clone ready!")
    print("📱 View at: http://localhost:8000/perfect_clone.html")
    print("🔄 The clone should now be indistinguishable from the original but with Legacy Estates branding!") 