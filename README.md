# 🚀 Playwright Python Automation Framework

## 📌 Overview

This project is an end-to-end test automation framework built using **Playwright + Pytest + API Testing + BDD**.

It covers:

* UI Automation
* API Automation
* Hybrid (API + UI) testing
* Data-driven testing
* BDD framework using pytest-bdd

---

## 🛠️ Tech Stack

* Python
* Playwright
* Pytest
* Pytest-BDD
* API Testing (requests)
* Page Object Model (POM)

---

## 📂 Project Structure

```
Playwright_Project/
│
├── data/                  # Test data (JSON)
├── features/              # BDD feature files
├── pageObjects/           # Page Object Model classes
├── utils/                 # API utilities
├── conftest.py            # Fixtures & setup
├── requirements.txt       # Dependencies
├── test_framework_web_api.py   # Hybrid test (API + UI)
├── test_pytest-bddTest.py      # BDD tests
├── test_web_api.py             # API tests
```

---

## 🔥 Key Features

* Hybrid testing (API + UI flow)
* Dynamic test data using JSON
* Parameterized tests using Pytest
* BDD implementation using pytest-bdd
* Cross-browser execution support
* HTML reporting
* Parallel execution using pytest-xdist

---

## ▶️ How to Run Tests

### Install dependencies

```
pip install -r requirements.txt
playwright install
```

### Run all tests

```
pytest
```

### Run specific test file

```
pytest test_framework_web_api.py
```

### Run with parallel execution

```
pytest -n 3
```

### Run with HTML report

```
pytest --html=report.html
```

---

## 📊 Sample Use Case

* Create order using API
* Login via UI
* Validate order in UI

---

## 📸 Test Execution & Reports

* Parallel execution using pytest-xdist
* HTML reports generated using pytest-html
* Playwright tracing enabled for debugging failures

## 🧪 Test Coverage

* UI Testing (Login, Order Flow)
* API Testing (Order Creation)
* Hybrid Testing (API + UI validation)
* BDD Scenarios using pytest-bdd

---

## 🚀 How this project stands out

* Combines API + UI testing in one flow
* Uses Page Object Model for maintainability
* Supports data-driven testing using JSON
* Includes BDD for readable test scenarios
* Designed for CI/CD integration

---

## 👩‍💻 Author

Anuja Shejwal
