# 🚀 OLKA Sprint Dashboard - GitHub Auto-Update Kurulum Rehberi

## 📋 İçindekiler
1. [Ön Gereksinimler](#ön-gereksinimler)
2. [ADIM 1: Jira API Token](#adım-1-jira-api-token)
3. [ADIM 2: GitHub Repository Hazırlama](#adım-2-github-repository-hazırlama)
4. [ADIM 3: GitHub Secrets Ekleme](#adım-3-github-secrets-ekleme)
5. [ADIM 4: GitHub Actions Aktivasyon](#adım-4-github-actions-aktivasyon)
6. [ADIM 5: Test ve Doğrulama](#adım-5-test-ve-doğrulama)
7. [Sorun Giderme](#sorun-giderme)

---

## ✅ Ön Gereksinimler

- GitHub hesabı (free olabilir)
- Jira hesabı (Atlassian Cloud)
- Git komut satırı (opsiyonel)

---

## 🔑 ADIM 1: Jira API Token

### 1.1 Token Oluştur

1. Git: https://id.atlassian.com/manage-profile/security/api-tokens
2. **"Create API token"** tıkla
3. Label: `GitHub Actions` yaz
4. **"Create"** tıkla
5. Token'ı **kopyala** (sonra görmeyeceksin!)

```
Örnek: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### 1.2 Email'ini Hazırla

Jira hesabında giriş yaptığın email:
```
example@example.com
```

---

## 📁 ADIM 2: GitHub Repository Hazırlama

### 2.1 Yeni Repository Oluştur

1. GitHub'da **"New"** → **"Repository"** tıkla
2. Ad: `olka-sprint-dashboard-live`
3. Description: `OLKA Sprint Dashboard - Auto-updating with Jira`
4. **Public** seç (GitHub Pages için gerekli)
5. **"Create repository"** tıkla

### 2.2 Dosyaları Yükle

Şu dosyaları repo'ya ekle:

#### A) `update_dashboard.py`
```python
# update_dashboard.py (yukarıda verilen dosya)
```

#### B) `.github/workflows/update.yml`
```yaml
# .github/workflows/update.yml (yukarıda verilen dosya)
```

#### C) `docs/index.html`
```html
<!-- Mevcut OLKA_Dashboard_Live.html'i kopyala -->
```

#### D) `README.md`
```markdown
# OLKA Sprint Dashboard

📊 Canlı sprint dashboard - Jira'dan otomatik güncellenecek

## 🌐 Dashboard URL

https://[your-username].github.io/olka-sprint-dashboard-live

## ⚙️ Kurulum

1. Jira API Token ekle
2. GitHub Secrets'a ekle
3. GitHub Pages'i aktif et

## 🔄 Otomatik Güncelleme

- Her 30 dakikada çalışır
- Jira'dan canlı veri çeker
- GitHub Pages'e yayınlar

---

## 🚀 ADIM 3: GitHub Secrets Ekleme

### 3.1 Settings'e Git

1. Repository → **"Settings"**
2. Sol menüde **"Secrets and variables"** → **"Actions"**
3. **"New repository secret"** tıkla

### 3.2 3 Secret Ekle

#### Secret 1: JIRA_EMAIL
- **Name:** `JIRA_EMAIL`
- **Value:** `your-email@example.com`
- **"Add secret"** tıkla

#### Secret 2: JIRA_API_TOKEN
- **Name:** `JIRA_API_TOKEN`
- **Value:** (ADIM 1'de kopyladığın token)
- **"Add secret"** tıkla

#### Secret 3: JIRA_CLOUD_ID
- **Name:** `JIRA_CLOUD_ID`
- **Value:** `501735f2-facf-4778-8cd4-8e1c19904057`
- **"Add secret"** tıkla

✅ Tüm 3 secret'ı eklersen artık görmeyeceksin!

---

## 📍 ADIM 4: GitHub Pages Aktivasyon

### 4.1 Settings'de GitHub Pages

1. Repository → **"Settings"**
2. Sol menüde **"Pages"**
3. **"Source"** → **"Deploy from a branch"** seç
4. Branch: **`main`** seç
5. Folder: **`/docs`** seç
6. **"Save"** tıkla

### 4.2 URL'ini Bul

```
https://[github-username].github.io/olka-sprint-dashboard-live
```

Örnek:
```
https://zeyneptopccuu.github.io/olka-sprint-dashboard-live
```

---

## ✅ ADIM 5: Test ve Doğrulama

### 5.1 Manual Trigger

1. Repository → **"Actions"** tab
2. **"🔄 Auto-Update OLKA Dashboard"** workflow tıkla
3. **"Run workflow"** → **"Run workflow"** tıkla
4. Workflow'u izle (1-2 dakika)

### 5.2 Logs Kontrol Et

```
✅ Checkout code
✅ Setup Python
✅ Install dependencies
✅ Update dashboard
✅ Configure Git
✅ Commit changes
✅ Deploy to GitHub Pages
✅ Publish to GitHub Pages
```

### 5.3 Dashboard'u Aç

1. Jira bağlantısı başarılıysa: **Full HTML dashboard** göreceksin
2. Jira bağlantısı başarısızsa: **Placeholder dashboard** göreceksin

---

## 🔄 Otomatik Çalışma

### Zamanlanmış Çalışma

```
Saat: Her 30 dakikada bir
Örnek: 00:00, 00:30, 01:00, 01:30, ...
```

### Manuel Trigger

```
Repository → Actions → Workflow → "Run workflow"
```

### Push Trigger

```
Git push her zaman workflow'u tetikler
```

---

## 🐛 Sorun Giderme

### Problem 1: "Action failed"

**Çözüm:**
1. Settings → Secrets kontrol et
2. JIRA_EMAIL ve JIRA_API_TOKEN doğru mu?
3. Workflow'u manuel trigger et

### Problem 2: "404 Not Found"

**Çözüm:**
1. GitHub Pages Settings kontrol et
2. Branch: `main`, Folder: `/docs`
3. 2-3 dakika bekle

### Problem 3: Jira bağlantısı başarısız

**Çözüm:**
1. API token'ı yenile
2. Email doğru mu kontrol et
3. Cloud ID doğru: `501735f2-facf-4778-8cd4-8e1c19904057`

### Problem 4: Workflow logs göremiyorum

**Çözüm:**
1. Repository → **"Actions"** tab
2. Workflow seç
3. İlgili job'u tıkla
4. "Run workflow" logs'u aç

---

## 📊 Dosya Yapısı

```
olka-sprint-dashboard-live/
├── .github/
│   └── workflows/
│       └── update.yml          # GitHub Actions workflow
├── docs/
│   └── index.html              # Dashboard (otomatik oluşur)
├── update_dashboard.py         # Update script
└── README.md                   # Bu dosya
```

---

## 🎯 Dashboard URL

Kurulumdan sonra:

```
https://[github-username].github.io/olka-sprint-dashboard-live
```

Bu URL'yi:
- Takım ile paylaş
- Mail'e koy
- Slack'te pin'le
- Bookmarks'a ekle

---

## 🔐 Security Notes

- **Secrets asla public değil** - GitHub otomatik enkripte eder
- **API Token'ı public commit'lemek istemiyorsan** - `.gitignore` kullan
- Repo public olsa da, secrets gizli kalır

---

## 📞 Destek

Sorun mu var?

1. GitHub Actions logs'u kontrol et
2. Secrets'ı doğrula
3. JIRA_API_TOKEN'ı yenile
4. Workflow'u manuel trigger et

---

## 🎉 Tamamlandı!

Dashboard'un artık:
- ✅ **Canlı** Jira verisi gösteriyor
- ✅ **Otomatik** güncelleniyor (30 dakika)
- ✅ **Herkes** erişebiliyor
- ✅ **Güvenli** GitHub Pages'de

🚀 **Başarılı kurulum!**
```

#### E) `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Secrets (opsiyonel, GitHub Secrets öneriliyor)
.env
.env.local
```

---

### 2.3 Git Push (Command Line)

```bash
cd olka-sprint-dashboard-live

# Dosyaları ekle
git add .

# Commit et
git commit -m "🚀 Initial commit - Auto-updating dashboard"

# Push et
git push -u origin main
```

Veya **GitHub Web UI** ile dosya yükle.

---

## 🔐 ADIM 3: GitHub Secrets Ekleme

### 3.1 Settings'e Git

1. Repository → **"Settings"**
2. Sol menüde: **"Secrets and variables"** → **"Actions"**

### 3.2 3 Secret Ekle

**Secret 1:**
```
Name: JIRA_EMAIL
Value: your-email@example.com
```

**Secret 2:**
```
Name: JIRA_API_TOKEN
Value: (a1b2c3d4e5f6... - ADIM 1'den)
```

**Secret 3:**
```
Name: JIRA_CLOUD_ID
Value: 501735f2-facf-4778-8cd4-8e1c19904057
```

---

## 🚀 ADIM 4: GitHub Pages Aktivasyon

1. Repository → **"Settings"**
2. Sol menü: **"Pages"**
3. **Source:** `Deploy from a branch`
4. **Branch:** `main`
5. **Folder:** `/docs`
6. **"Save"** tıkla

**Dashboard URL:**
```
https://[your-username].github.io/olka-sprint-dashboard-live
```

---

## ✅ ADIM 5: Test Et

1. Repository → **"Actions"** tab
2. **"🔄 Auto-Update OLKA Dashboard"** tıkla
3. **"Run workflow"** → **"Run workflow"** tıkla
4. Logs'u izle

**Başarılı olursa:**
- ✅ Workflow yeşil
- ✅ docs/index.html güncellendi
- ✅ GitHub Pages yayınlandı

---

## 📊 Otomatik Çalışma

```
⏰ Her 30 dakikada
🔄 Jira'dan veri çeker
🎨 HTML oluşturur
📤 GitHub'a push eder
🌐 GitHub Pages'e yayınlar
```

---

## 🎉 Hazır!

```
✅ Kurulum tamamlandı
✅ Dashboard canlı
✅ Otomatik güncelleniyor
✅ Herkes erişebiliyor
```

**Dashboard linki:**
```
https://[your-username].github.io/olka-sprint-dashboard-live
```

---

**Soru var mı?** Her adımı kontrol et! 🚀
