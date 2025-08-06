import re
import os

def fix_branding_completely():
    """Fix all remaining branding issues to make it truly indistinguishable"""
    
    print("🎯 Fixing all branding issues for perfect clone...")
    
    # Read the current perfect clone
    with open('perfect_clone.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Comprehensive replacements for all branding
    replacements = {
        # Logo and main headings
        'EMPIRELEGACY': 'LEGACYESTATES',
        'EMPIRE LEGACY': 'LEGACY ESTATES',
        'Empire Legacy': 'Legacy Estates',
        'Empire Legacy In Thorold': 'Legacy Estates In Thorold',
        'Why Empire Legacy In Thorold?': 'Why Legacy Estates In Thorold?',
        
        # Company references
        'Empire Communities': 'Legacy Communities',
        'Empire Canals': 'Legacy Canals',
        'Empire 30': 'Legacy 30',
        
        # Content improvements
        'first master-planned community': 'premier master-planned community',
        'new townhouse and single family home development': 'luxury townhouse and single family home development',
        'highly desirable master-planned community': 'premium master-planned community',
        'over 1,000 new townhomes and detached homes': 'over 1,000 luxury townhomes and detached homes',
        'scenic city of Welland': 'prestigious city of Welland',
        
        # Investment references
        'We have personally invested in and sold hundreds of homes in previous Empire master-planned communities': 'We have personally invested in and sold hundreds of homes in previous Legacy master-planned communities',
        'Empire has successfully built these communities': 'Legacy has successfully built these communities',
        'Empire has received prestigious awards': 'Legacy has received prestigious awards',
        'Empire\'s relentless pursuit of excellence': 'Legacy\'s relentless pursuit of excellence',
        
        # Map and location references
        'Legacy | Empire Homes': 'Legacy | Legacy Homes',
        'Empire%20Legacy%20%7C%20Empire%20Communities': 'Legacy%20Estates%20%7C%20Legacy%20Communities',
        
        # Disclaimer and legal text
        'Empire Communities\' trademarks': 'Legacy Communities\' trademarks',
        'Unauthorized use of Empire Communities\' trademarks': 'Unauthorized use of Legacy Communities\' trademarks',
        'Any unauthorized use of Empire Communities\' trademarks': 'Any unauthorized use of Legacy Communities\' trademarks',
        
        # Links and references
        'empirecanals.ca': 'legacycanals.ca',
        'WWW.EMPIRECANALS.CA': 'WWW.LEGACYCANALS.CA',
        'WWW.WYNDFIELDEMPIRE.COM': 'WWW.WYNDFIELDLEGACY.COM',
        
        # Meta descriptions and titles
        'Empire Legacy is Thorold\'s first master-planned community': 'Legacy Estates is Thorold\'s premier master-planned community',
        'Empire Legacy is a new townhouse and single family home development By Empire Communities': 'Legacy Estates is a luxury townhouse and single family home development By Legacy Communities',
        
        # Keywords and SEO
        'Empire Legacy Thorold,Empire Legacy,Empire Thorold,Legacy Thorold,Niagara Homes': 'Legacy Estates Thorold,Legacy Estates,Legacy Thorold,Niagara Homes',
        
        # Schema markup
        '"name":"Empire Canals : Platinum Access"': '"name":"Legacy Canals : Platinum Access"',
        '"caption":"Empire Canals : Platinum Access"': '"caption":"Legacy Canals : Platinum Access"',
        '"name":"Legacy Canals : Platinum Access"': '"name":"Legacy Canals : Platinum Access"',
        
        # RSS feeds
        'Empire Legacy - Thorold » Feed': 'Legacy Estates - Thorold » Feed',
        'Empire Legacy - Thorold » Comments Feed': 'Legacy Estates - Thorold » Comments Feed',
        
        # Image alt text
        'New Homes at Empire Canal': 'New Homes at Legacy Canal',
        'Empire Legacy Logo': 'Legacy Estates Logo',
        'Empire Legacy Floorplans': 'Legacy Estates Floorplans',
        'Master-Planned Community': 'Master-Planned Community',
        'New Homes at Legacy Canal': 'New Homes at Legacy Canal',
        'Population Growth': 'Population Growth',
        'Legacy Communities Logo': 'Legacy Communities Logo',
        'Legacy Estates': 'Legacy Estates',
        'Legacy Canals': 'Legacy Canals',
        'Wyndfield Legacy': 'Wyndfield Legacy',
        'Legacy Communities': 'Legacy Communities',
        'WhatsApp Contact': 'WhatsApp Contact',
    }
    
    # Apply all replacements
    for old_text, new_text in replacements.items():
        html_content = html_content.replace(old_text, new_text)
    
    # Additional regex replacements for more complex patterns
    # Fix any remaining Empire references in text content
    html_content = re.sub(r'\bEmpire\b(?!\s+Legacy)', 'Legacy', html_content, flags=re.IGNORECASE)
    
    # Fix any remaining "Empire Legacy" that might have been missed
    html_content = re.sub(r'Empire\s+Legacy', 'Legacy Estates', html_content, flags=re.IGNORECASE)
    
    # Fix any remaining "Empire Communities" that might have been missed
    html_content = re.sub(r'Empire\s+Communities', 'Legacy Communities', html_content, flags=re.IGNORECASE)
    
    # Save the completely fixed version
    with open('perfect_clone_fixed.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ All branding issues fixed!")
    print("🎯 The clone should now be completely indistinguishable with Legacy Estates branding!")
    
    return True

def create_final_perfect_clone():
    """Create the final perfect clone with all fixes applied"""
    
    print("🚀 Creating final perfect clone...")
    
    # Apply all branding fixes
    fix_branding_completely()
    
    # Copy the fixed version to the main index
    os.system("cp perfect_clone_fixed.html index.html")
    
    print("✅ Final perfect clone created!")
    print("📱 View at: http://localhost:8000")
    print("🎯 This should now be completely indistinguishable from the original but with Legacy Estates branding!")

if __name__ == "__main__":
    create_final_perfect_clone() 