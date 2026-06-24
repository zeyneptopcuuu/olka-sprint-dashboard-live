name: 🔄 Auto-Update OLKA Dashboard

on:
  schedule:
    # Her 30 dakikada çalış
    - cron: '*/30 * * * *'
  
  # Manuel trigger
  workflow_dispatch:
  
  # Her push'ta
  push:
    branches:
      - main

jobs:
  update-dashboard:
    runs-on: ubuntu-latest
    
    permissions:
      contents: write
      pages: write
      id-token: write
    
    steps:
      # 1. Repository'yi clone et
      - name: 📥 Checkout code
        uses: actions/checkout@v4
      
      # 2. Python ayarla
      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      
      # 3. Dependencies yükle
      - name: 📦 Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests
      
      # 4. Dashboard'u güncelle
      - name: 🎨 Update dashboard
        env:
          JIRA_CLOUD_ID: ${{ secrets.JIRA_CLOUD_ID }}
          JIRA_EMAIL: ${{ secrets.JIRA_EMAIL }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
        run: |
          python update_dashboard.py
      
      # 5. Git config
      - name: 🔧 Configure Git
        run: |
          git config --local user.email "github-actions@github.com"
          git config --local user.name "GitHub Actions"
      
      # 6. Commit ve push et
      - name: 📤 Commit changes
        run: |
          if git diff-index --quiet HEAD; then
            echo "✅ No changes to commit"
          else
            git add docs/index.html
            git commit -m "🔄 Auto-update dashboard - $(date +'%Y-%m-%d %H:%M:%S')"
            git push
          fi
  
  # GitHub Pages deployment
  deploy-pages:
    needs: update-dashboard
    runs-on: ubuntu-latest
    
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    
    permissions:
      contents: read
      pages: write
      id-token: write
    
    steps:
      # 1. Repository'yi clone et
      - name: 📥 Checkout code
        uses: actions/checkout@v4
        with:
          ref: main
      
      # 2. GitHub Pages'e upload et
      - name: 🚀 Upload pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'docs'
      
      # 3. Deploy
      - name: 📍 Publish to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
      
      # 4. Notification
      - name: ✨ Success
        run: |
          echo "✅ Dashboard güncellendi ve yayınlandı!"
          echo "🌐 URL: ${{ steps.deployment.outputs.page_url }}"
