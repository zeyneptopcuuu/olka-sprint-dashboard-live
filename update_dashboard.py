name: Auto-Update Dashboard

on:
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Create Dashboard
        run: |
          mkdir -p docs
          echo '<!DOCTYPE html>
          <html lang="tr">
          <head>
            <meta charset="UTF-8">
            <title>OLKA Sprint Dashboard</title>
          </head>
          <body style="background:#f4f5f7;padding:20px">
            <div style="max-width:760px;margin:0 auto;background:white;padding:30px;border:1px solid #e2e4e8">
              <h1 style="color:#14532d">OLKA Sprint Dashboard Live</h1>
              <p> Dashboard aktif!</p>
              <p>Güncelleme: '$(date)' </p>
            </div>
          </body>
          </html>' > docs/index.html
      
      - name: Push
        run: |
          git config user.email "bot@github.com"
          git config user.name "Bot"
          git add docs/index.html
          git commit -m "Update" || true
          git push || true
