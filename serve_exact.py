import http.server
import socketserver
import os
import shutil

def setup_exact_clone():
    """Set up the exact clone for serving"""
    
    print("🎯 Setting up exact website clone...")
    
    # Copy all files from exact_clone to current directory
    if os.path.exists("exact_clone"):
        for file in os.listdir("exact_clone"):
            src = os.path.join("exact_clone", file)
            dst = os.path.join(".", file)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"✅ Copied: {file}")
    
    print("✅ Exact clone setup complete!")

def serve_website(port=8000):
    """Serve the website on the specified port"""
    
    print(f"🚀 Starting server on port {port}...")
    print(f"📱 Open your browser and go to: http://localhost:{port}")
    print("🛑 Press Ctrl+C to stop the server")
    
    # Change to the directory with the website files
    os.chdir(".")
    
    # Create and start the server
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"✅ Server running at http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    setup_exact_clone()
    serve_website() 