# 🎯 Playwright Python Automation (POM + Reports)

This project uses **Playwright (Python)** with **Pytest** and **Page Object Model (POM)**.  
It automates a simple **login test on [saucedemo.com](https://www.saucedemo.com)** and supports both **HTML** and **Allure** reports.

---

## ⚙️ Setup & Installation

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies

requirements.txt
```bash
pytest==8.3.3
playwright==1.49.0
pytest-playwright==0.5.0
pytest-html==4.1.1
allure-pytest==2.13.5
pytest-metadata==3.1.1
```
```bash
pip install -r requirements.txt
python -m playwright install
```
### Project Structure
```bash
project/
├── pages/login_page.py
├── tests/test_login.py
├── conftest.py
└── requirements.txt
```
### 🧠 Record Test with Codegen
```bash
playwright codegen https://www.saucedemo.com/
```
Interact and copy generated Python code to your POM class or test.

### 🧪 Run Tests
```bash
pytest -v
```
Run Specific File:
```bash
pytest tests/test_login.py
pytest test_login.py
```

### 🧾 HTML Report Generate
```bash
pytest --html=reports/report.html --self-contained-html
```

### 🧾 Allure Report Generate 
Install Allure CLI:
```bash
iwr -useb get.scoop.sh | iex
scoop install allure
```
Generate & View:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

