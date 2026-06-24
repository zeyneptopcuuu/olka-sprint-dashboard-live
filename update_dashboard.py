#!/usr/bin/env python3
"""
OLKA Sprint Dashboard - Auto-Update Script
Simply copies and updates the dashboard
"""

import os
import shutil
from datetime import datetime

print("🚀 Starting dashboard update...")

# Create docs directory
os.makedirs('docs', exist_ok=True)

# Copy HTML file
try:
    if os.path.exists('OLKA_Dashboard_Live.html'):
        shutil.copy('OLKA_Dashboard_Live.html', 'docs/index.html')
        print("✅ Dashboard copied successfully")
    else:
        print("⚠️ HTML file not found, creating default...")
        with open('docs/index.html', 'w') as f:
            f.write('<h1>OLKA Dashboard</h1><p>Updated: ' + str(datetime.now()) + '</p>')
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

print("✅ Update complete!")
