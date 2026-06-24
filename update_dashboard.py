#!/usr/bin/env python3
import os
from datetime import datetime

os.makedirs('docs', exist_ok=True)

html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>OLKA Sprint Dashboard</title>
</head>
<body style="background:#f4f5f7;padding:20px">
    <div style="max-width:760px;margin:0 auto;background:white;padding:30px;border:1px solid #e2e4e8">
        <h1 style="color:#14532d">OLKA Sprint Dashboard Live</h1>
        <p>✅ Dashboard aktif!</p>
        <p>Güncelleme: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>"""

with open('docs/index.html', 'w') as f:
    f.write(html)

print("✅ Dashboard created!")
