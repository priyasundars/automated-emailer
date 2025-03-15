# 📊 RBI Rate Scraper & Email Notifier 🔔

_A Python automation tool that scrapes financial rates from the Reserve Bank of India and sends formatted email alerts_

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Jinja2](https://img.shields.io/badge/Templating-Jinja2-green)](https://jinja.palletsprojects.com)
[![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup4-yellowgreen)](https://www.crummy.com/software/BeautifulSoup/)

## 🌟 Features
- Real-time scraping of RBI financial rates
- Automated email notifications with clean HTML formatting
- Environment variable configuration for secure credentials
- Responsive email template design
- Error handling for email delivery
- Rate data normalization and cleaning

## 🚀 How It Works
1. **Web Scraping** ✨  
   Fetches latest rates from RBI website using BeautifulSoup
2. **Data Transformation** 🔄  
   Cleans and structures scraped data into key-value pairs
3. **Email Templating** 📧  
   Uses Jinja2 to create professional HTML templates
4. **Secure Delivery** 🔒  
   Sends emails via SMTP with .env credentials

## ⚙️ Installation
```bash
pip install -r requirements.txt
```
**Requirements:**
```text
beautifulsoup4==4.12.2
python-dotenv==1.0.0
Jinja2==3.1.2
requests==2.31.0
```

## 🔧 Configuration
1. Create `.env` file:
```ini
SMTP_USERNAME="your@email.com"
SMTP_PASSWORD="your_app_password"
```
2. Set recipients in `main.py`:
```python
recipients = ["important.person@company.com", "finance.team@org.com"]
```

## 🖥️ Usage
```bash
python main.py
```
**Sample Output:**
```
✅ Data retrieved from RBI
📨 Emails sent successfully to 2 recipients!
```

## 📂 Project Structure
```
.
├── main.py                 # Main workflow controller
├── templates/
│   └── template.html       # Stylish email template
├── utils/
│   ├── parse.py            # RBI scraper module
│   └── send_emails.py      # Secure email delivery
└── .env.example            # Configuration template
```

## ⚠️ Disclaimer
This project is for educational purposes only. Always verify RBI rates from official sources.

## 📜 License
MIT License - Use responsibly and respect RBI's website terms of service.

---

_Crafted with ❤️ by priyasundar 
