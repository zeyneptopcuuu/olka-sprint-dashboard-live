#!/usr/bin/env python3
"""
OLKA Sprint Dashboard - Auto-Update Script
Updates dashboard timestamp and commits to GitHub
"""

import os
import shutil
from datetime import datetime

def main():
    print("🚀 OLKA Sprint Dashboard - Auto-Update Started")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ensure docs directory exists
    os.makedirs('docs', exist_ok=True)
    
    # Copy dashboard HTML
    try:
        if os.path.exists('OLKA_Dashboard_Live.html'):
            shutil.copy('OLKA_Dashboard_Live.html', 'docs/index.html')
            print("✅ Dashboard copied to docs/index.html")
        else:
            print("⚠️ OLKA_Dashboard_Live.html not found, creating placeholder")
            create_placeholder()
    except Exception as e:
        print(f"❌ Error copying dashboard: {e}")
        create_placeholder()
    
    print("✨ Done!")

def create_placeholder():
    """Create a simple placeholder dashboard"""
    html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>OLKA Sprint Dashboard</title>
</head>
<body style="background:#f4f5f7; font-family:'Segoe UI', sans-serif; margin:0; padding:20px;">
    <div style="max-width:760px; margin:0 auto; background:white; padding:30px; border:1px solid #e2e4e8;">
        <h1 style="color:#14532d; border-bottom:3px solid #2e8b57; padding-bottom:10px;">
            OLKA Sprint Dashboard Live
        </h1>
        <p style="color:#666;">
            📊 Jira canlı verisi otomatik olarak güncellenmektedir.<br>
            ⏰ Son güncelleme: <span id="update-time"></span><br>
            🔄 Sonraki güncelleme: 30 dakika içinde
        </p>
    </div>
    <script>
        document.getElementById('update-time').textContent = new Date().toLocaleString('tr-TR');
    </script>
</body>
</html>"""
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Placeholder dashboard created")

if __name__ == '__main__':
    main()
