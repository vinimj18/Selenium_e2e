# 🛒 E-commerce Website – End-to-End Testing with Selenium + Python

This project demonstrates an automated end-to-end test suite for a sample e-commerce website using **Selenium WebDriver**, **Python**, and **PyTest**. The suite covers critical user journeys such as logging in, searching for products, adding items to the cart, and completing the checkout process.

## 🔍 Features Covered

- ✅ **Login** – Valid and invalid credential handling
- 🔎 **Product Search** – Searching for items by name
- 🛒 **Add to Cart** – Adding single and multiple items
- 💳 **Checkout** – Proceeding through the checkout process with form validations

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Automation Tool:** Selenium WebDriver  
- **Test Runner:** PyTest  
- **Design Pattern:** Page Object Model (POM)  
- **Test Strategy:** Data-driven Testing  
- **Locator Strategies:** XPath, CSS Selectors  

## 📁 Project Structure
```
Selenium_e2e/
│
├── tests/ # Test files organized by feature
│ ├── test_login.py
│ ├── test_search.py
│ └── test_checkout.py
│
├── pages/ # Page Object classes for each screen
│ ├── login_page.py
│ ├── search_page.py
│ └── checkout_page.py
│
├── data/ # Test data files (CSV, JSON, etc.)
│
├── conftest.py # PyTest fixtures and setup
├── requirements.txt # Project dependencies
└── README.md
```
## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/vinimj18/Selenium_e2e.git
cd Selenium_e2e
```
2. Create a virtual environment
```bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```
3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
4. Run the test suite
```bash
Copy
Edit
pytest tests/
```
Tip: Use pytest -v for verbose output or pytest --html=report.html if using a reporting plugin.

📌 Highlights
- Modular and maintainable test structure using Page Object Model
- Reusable fixtures and test data
- Easily extensible for additional scenarios
- Built to mimic real-world testing workflows

📄 License
This project is licensed under the MIT License. Feel free to fork, contribute, or adapt it for your own learning and projects.

👤 Author
Vinicius Maggiotto Justen
LinkedIn • GitHub
