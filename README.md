# 🏡 Zillow Data Scraper & Google Form Auto-Filler

This Python automation script scrapes property listings from Zillow using `BeautifulSoup` and fills a Google Form with each listing's address, price, and link using `Selenium`.

## 🚀 Features

- Extracts **address**, **price**, and **property link** from Zillow listings
- Automatically fills out a **Google Form** for each property
- Uses `requests` and `bs4` (BeautifulSoup) for fast scraping
- Uses `Selenium` for browser-based automation
- Works with environment variables for secure configuration

## 🧰 Tech Stack

- Python 🐍
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium](https://www.selenium.dev/)
- [Google Forms](https://www.google.com/forms/about/)
- [Zillow](https://www.zillow.com/)
- `.env` file via `python-dotenv`

## 📦 Installation

1. Clone this repository  
   ```bash
   git clone https://github.com/SD1107/zillow-form-bot.git
   cd zillow-form-bot
