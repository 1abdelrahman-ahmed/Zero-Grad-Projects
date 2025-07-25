
# 🕸️ Wuzzuf Job Scraper

A simple web scraping project that collects job postings from Wuzzuf.com based on selected topics such as Data Science, Machine Learning, and Artificial Intelligence.

---

## 📋 Project Description

This script scrapes job listings from [Wuzzuf](https://wuzzuf.net) for the following keywords:

- **Data Science**
- **Machine Learning**
- **Artificial Intelligence**

It extracts information such as:
- Job Title
- Link to the job post
- Occupation Type (Full Time, Remote, etc.)
- Company Name
- Job Location
- Job Description / Specs

The results are saved into a single CSV file: `data.csv`

---

## 🔧 How It Works

### 🧩 Main Functions

- `scrape_pages(topic)`: Scrapes all pages for a given search keyword.
- `combine_dicts(dicts)`: Combines multiple scraped dictionaries into one.
- `combine_dfs(dfs)`: Merges all DataFrames and removes duplicates.

### 🗂 Output

All job data is saved to:
```
data.csv
```

---

## ▶️ How to Run

1. Install required libraries:
```bash
pip install requests beautifulsoup4 lxml pandas
```

2. Run the main script:
```bash
python main.py
```

---

## 🛠️ Built With

- Python 3
- Requests
- BeautifulSoup (bs4)
- Pandas

---

## ⚠️ Disclaimer

This project is for educational purposes only. Wuzzuf's structure may change over time, so scraping might break if the website updates its layout.

---

## 📄 License

This project is open-source and free to use.
