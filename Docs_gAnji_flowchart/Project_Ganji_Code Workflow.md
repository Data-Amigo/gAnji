# 🚀 Project Ganji – AI Scraper (POC)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black)
![Status](https://img.shields.io/badge/Status-POC-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

**Project Ganji** is a data-driven system designed to collect and analyze prediction data from platforms such as betting sites and forecasting markets.

This repository contains **Phase 1 (POC)** — an **AI-powered web scraper** that:

- 🌐 Scrapes dynamic websites using Bright Data + Selenium
- 🧹 Cleans and processes HTML content
- 🧠 Uses an LLM (LLaMA 3 via Ollama) to extract structured data
- 🖥️ Provides an interactive UI via Streamlit

---

## 🧱 Architecture

```
[ Web Source ]
    ↓
[ Selenium + Bright Data Proxy ]
    ↓
[ BeautifulSoup Processing ]
    ↓
[ Ollama (LLM Parsing) ]
    ↓
[ Streamlit UI ]
```

---

## 🎥 Demo Flow

### Step 1: Enter URL
```
https://forebet.com
```

### Step 2: Scrape Website
- Extracts full rendered HTML
- Cleans and displays readable content

### Step 3: Define Extraction Task
```
Extract all football match predictions and odds
```

### Step 4: AI Output
```
Team A vs Team B - Prediction: 2-1
Odds: 1.85
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/project-ganji.git
cd project-ganji
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Make sure Ollama is installed and running:

```bash
ollama run llama3
```

### 5. Configure Bright Data

Create a `.streamlit/secrets.toml` file:

```toml
AUTH = "your_brightdata_auth"
```

---

## ▶️ Running the App

```bash
streamlit run ai_scrapper_app.py
```

---

## 📂 Project Structure

```
project-ganji/
│
├── scrape.py              # Scraping logic (Selenium + Bright Data)
├── llm_parse.py           # LLM parsing logic (Ollama)
├── ai_scrapper_app.py     # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 🧠 Key Features

### 🔹 AI-Based Parsing
No need for fragile CSS selectors — just describe what you want.

### 🔹 Dynamic Site Support
Handles JavaScript-heavy sites via Selenium.

### 🔹 Modular Pipeline
Easily extendable to:
- Databases
- APIs
- Prediction engines

---

## ⚠️ Limitations (POC)

- 💸 Limited Bright Data credits
- 🐢 Sequential LLM processing (slow)
- 📄 Output is unstructured text
- ❌ No database integration yet

---

## 🚀 Roadmap

- [ ] Structured JSON output
- [ ] PostgreSQL integration
- [ ] Async / parallel scraping
- [ ] Cost optimization layer
- [ ] Prediction engine (core of Ganji)

---

## 💡 Core Idea

> Instead of writing scraping rules, you describe the data — and the AI extracts it.

---

## 🧩 Future Architecture

```
Scraper → PostgreSQL → Prediction Engine → Insights Dashboard
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Fred Muigai

---

⭐ If you like this project, consider giving it a star!