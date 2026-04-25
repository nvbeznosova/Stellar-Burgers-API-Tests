# Stellar Burgers — API Test Automation

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.4+-orange.svg)](https://docs.pytest.org/)
[![requests](https://img.shields.io/badge/requests-2.31+-green.svg)](https://docs.python-requests.org/)
[![Allure](https://img.shields.io/badge/Allure-2.13-purple.svg)](https://docs.qameta.io/allure/)

Automated API tests for [Stellar Burgers](https://stellarburgers.nomoreparties.site/) — a burger constructor service.  
The project covers user creation, login, and order placement endpoints.

## Project Description

This project contains automated API tests built with **pytest** and the **requests** library.  
It uses **Allure** for detailed test reports and follows a structured approach with separate helpers, URL configuration, and conftest fixtures.

## Test Coverage

### User Creation
- Create a unique user
- Create a user that already exists (expect error)
- Create a user with missing required fields (expect error)

### User Login
- Login with existing user (positive)
- Login with incorrect login/password (negative)

### Order Creation
- Create order with authorization
- Create order without authorization
- Create order with ingredients
- Create order without ingredients (expect error)
- Create order with invalid ingredient hash (expect error)

## Bug Found

While testing order creation without authorization, the following discrepancy was discovered:

| Expected | Actual |
|----------|--------|
| Attempting to create an order without the `Authorization` header should return `401 Unauthorized`. | The API returns `200 OK` and creates a guest order. |

*Status: bug, requires clarification with developers.*

## Project Structure

```
Stellar-Burgers-API-Tests/
        ├── README.md
        ├── conftest.py
        ├── helpers.py
        ├── requirements.txt
        ├── urls.py
        └── tests/
            ├── test_login.py
            ├── test_order.py
            └── test_user.py
```

## Setup & Installation

### Requirements
- Python 3.12+
- pytest
- requests
- allure-pytest

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nvbeznosova/Stellar-Burgers-API-Tests.git
   cd Stellar-Burgers-API-Tests
   ```

2.  **Create and activate a virtual environment** 
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   # .venv\Scripts\activate    # On Windows
   ``` 

3. **Install dependencies**
```bash 
   pip install -r requirements.txt 
   ``` 

## Running Tests 

1. **Run all tests**

```bash
   pytest tests/
   ```

2. **Run a specific test file**
```bash
   pytest tests/test_user.py
   ```

3. **Run with Allure results**
```bash
pytest --alluredir=allure-results tests/
```

## Allure Reports

1. **Generate report**
```bash
allure serve allure-results 
```

In CI/CD (GitHub Actions) the report can be automatically published to GitHub Pages.

