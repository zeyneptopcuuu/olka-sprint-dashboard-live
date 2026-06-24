#!/usr/bin/env python3
"""
OLKA Sprint Dashboard - Auto-Update Script
Fetches live Jira data and generates HTML dashboard
"""

import os
import json
import requests
from datetime import datetime
from base64 import b64encode

# ==================== CONFIGURATION ====================

JIRA_CLOUD_ID = os.getenv('JIRA_CLOUD_ID', '501735f2-facf-4778-8cd4-8e1c19904057')
JIRA_EMAIL = os.getenv('JIRA_EMAIL', 'your-email@example.com')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN', 'your-api-token')
JIRA_PROJECT = 'EWT'
SPRINT_CUSTOM_FIELD = 'customfield_10020'

# ==================== JIRA API FUNCTIONS ====================

def get_jira_headers():
    """Create Jira API auth headers"""
    credentials = b64encode(f'{JIRA_EMAIL}:{JIRA_API_TOKEN}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

def fetch_jira_data():
    """Fetch active sprint data from Jira"""
    try:
        jql = f'project = {JIRA_PROJECT} AND sprint in openSprints() ORDER BY issuetype ASC, status ASC'
        
        url = f'https://olkaproduct.atlassian.net/rest/api/3/search'
        
        params = {
            'jql': jql,
            'maxResults': 100,
            'fields': [
                'summary', 'status', 'issuetype', 'labels', 'duedate',
                'resolutiondate', 'priority', 'assignee', SPRINT_CUSTOM_FIELD,
                'created'
            ]
        }
        
        response = requests.get(
            url,
            params=params,
            headers=get_jira_headers(),
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Fetched {len(data.get('issues', []))} issues from Jira")
            return data.get('issues', [])
        else:
            print(f"⚠️ Jira API error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error fetching Jira data: {str(e)}")
        return None

def process_jira_issues(issues):
    """Process Jira issues into dashboard format"""
    if not issues:
        return {
            'total': 0,
            'by_brand': {},
            'by_status': {},
            'issues': []
        }
    
    brands = {
        'Skechers': [],
        'Mobile': [],
        'Klaud': [],
        'High5': [],
        'Brooks': [],
        'Hunter': [],
        'Steve Madden': []
    }
    
    statuses = {}
    
    for issue in issues:
        key = issue.get('key', 'N/A')
        summary = issue.get('fields', {}).get('summary', 'N/A')
        status = issue.get('fields', {}).get('status', {}).get('name', 'UNKNOWN')
        issuetype = issue.get('fields', {}).get('issuetype', {}).get('name', 'N/A')
        priority = issue.get('fields', {}).get('priority', {}).get('name', 'Medium')
        assignee = issue.get('fields', {}).get('assignee', {})
        assignee_name = assignee.get('displayName', 'Unassigned') if assignee else 'Unassigned'
        labels = issue.get('fields', {}).get('labels', [])
        
        # Detect brand
        brand = 'Mobile' if any(x in str(labels).lower() for x in ['mobile', 'ios', 'android']) else 'Skechers'
        if 'klaud' in str(labels).lower():
            brand = 'Klaud'
        elif 'high5' in str(labels).lower():
            brand = 'High5'
        elif 'brooks' in str(labels).lower():
            brand = 'Brooks'
        elif 'hunter' in str(labels).lower():
            brand = 'Hunter'
        elif 'steve madden' in str(labels).lower():
            brand = 'Steve Madden'
        
        issue_obj = {
            'key': key,
            'summary': summary,
            'status': status,
            'type': issuetype,
            'priority': priority,
            'brand': brand,
            'assignee': assignee_name,
            'labels': labels
        }
        
        brands[brand].append(issue_obj)
        
        if status not in statuses:
            statuses[status] = []
        statuses[status].append(issue_obj)
    
    return {
        'total': len(issues),
        'by_brand': brands,
        'by_status': statuses,
        'issues': issues
    }

# ==================== HTML GENERATION ====================

def generate_html(data, jira_issues_raw=None):
    """Generate HTML dashboard from data"""
    
    # Use existing HTML if Jira API fails
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>OLKA Sprint Dashboard Live</title>
</head>
<body style="background:#f4f5f7; font-family:'Segoe UI', sans-serif; margin:0; padding:20px;">
    <div style="max-width:760px; margin:0 auto; background:white; padding:30px; border:1px solid #e2e4e8;">
        <h1 style="color:#14532d; border-bottom:3px solid #2e8b57; padding-bottom:10px;">
            OLKA Sprint Dashboard — Live
        </h1>
        <p style="color:#666;">
            📊 Jira canlı verisi otomatik olarak güncellenmektedir.<br>
            ⏰ Son güncelleme: <span id="update-time"></span><br>
            🔄 Sonraki güncelleme: 30 dakika içinde
        </p>
        <div style="background:#f0f0f0; padding:20px; border-left:4px solid #2e8b57;">
            <p><strong>✅ Dashboard aktif ve çalışıyor!</strong></p>
            <p>Jira API bağlantısı konfigüre edildikten sonra, tüm sprint verileri burada gösterilecektir.</p>
        </div>
    </div>
    <script>
        document.getElementById('update-time').textContent = new Date().toLocaleString('tr-TR');
    </script>
</body>
</html>"""
    
    # Update timestamp
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # Insert update time
    html = html.replace(
        '<span id="update-time"></span>',
        f'<span id="update-time">{timestamp}</span>'
    )
    
    return html

# ==================== GITHUB COMMIT ====================

def commit_to_github():
    """Commit updated dashboard to GitHub"""
    try:
        import subprocess
        
        # Git config
        subprocess.run(['git', 'config', 'user.email', 'github-actions@github.com'], check=True)
        subprocess.run(['git', 'config', 'user.name', 'GitHub Actions'], check=True)
        
        # Add and commit
        subprocess.run(['git', 'add', 'docs/index.html'], check=True)
        
        # Check if there are changes
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        
        if result.stdout.strip():
            commit_msg = f"🔄 Auto-update dashboard - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            subprocess.run(['git', 'push'], check=True)
            print("✅ Pushed to GitHub")
            return True
        else:
            print("ℹ️ No changes to commit")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error committing to GitHub: {e}")
        return False

# ==================== MAIN ====================

def main():
    print("🚀 OLKA Sprint Dashboard - Auto-Update Started")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Fetch Jira data
    print("\n📡 Fetching Jira data...")
    jira_issues = fetch_jira_data()
    
    # Process data
    print("\n📊 Processing sprint data...")
    sprint_data = process_jira_issues(jira_issues) if jira_issues else None
    
    # Generate HTML
    print("\n🎨 Generating HTML dashboard...")
    html_content = generate_html(sprint_data, jira_issues)
    
    # Ensure docs directory exists
    os.makedirs('docs', exist_ok=True)
    
    # Write HTML
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Dashboard generated: docs/index.html")
    
    # Commit to GitHub
    print("\n📤 Committing to GitHub...")
    commit_to_github()
    
    print("\n✨ Done!")

if __name__ == '__main__':
    main()
