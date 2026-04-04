# REST API Testing Framework

![Python](https://img.shields.io/badge/Python-3.9-blue)
![requests](https://img.shields.io/badge/requests-2.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen)
![Tests](https://img.shields.io/badge/Tests-19%20Passing-success)
![API](https://img.shields.io/badge/API-REST-blue)

Comprehensive REST API testing framework built with Python 
requests library and pytest. Tests JSONPlaceholder REST API 
covering all HTTP methods — GET, POST, PUT and DELETE — 
with status code validation, JSON schema verification 
and response time testing across 19 automated test cases.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Primary programming language |
| requests | HTTP library for API calls |
| pytest | Test framework and execution |
| pytest-html | HTML test report generation |
| GitHub Actions | CI/CD — auto runs tests on every push |

---

## Project Structure
api-testing-framework/
├── utils/
│   ├── init.py
│   └── api_client.py        # Reusable API helper class
├── tests/
│   ├── init.py
│   ├── test_posts.py        # Posts endpoint tests (7)
│   ├── test_users.py        # Users endpoint tests (6)
│   └── test_todos.py        # Todos endpoint tests (6)
├── reports/
│   └── report.html          # Generated HTML report
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions workflow
├── conftest.py
├── requirements.txt
└── .gitignore

---

## API Under Test

**JSONPlaceholder** — Free fake REST API for testing
Base URL: https://jsonplaceholder.typicode.com
Endpoints tested:
/posts    → Blog posts (100 records)
/users    → Users (10 records)
/todos    → Todo items (200 records)

---

## Test Cases (19 Total)

### Posts API — 7 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_posts | GET | Fetch all 100 posts | Positive |
| test_get_single_post | GET | Fetch post by ID | Positive |
| test_create_post | POST | Create new post | Positive |
| test_update_post | PUT | Update existing post | Positive |
| test_delete_post | DELETE | Delete a post | Positive |
| test_invalid_post | GET | Non-existent post (404) | Negative |
| test_response_time | GET | Response under 2 seconds | Performance |

### Users API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_users | GET | Fetch all 10 users | Positive |
| test_get_single_user | GET | Fetch user by ID | Positive |
| test_user_has_required_fields | GET | Schema validation | Positive |
| test_user_email_format | GET | Email contains @ | Positive |
| test_invalid_user | GET | Non-existent user (404) | Negative |
| test_user_response_time | GET | Response under 2 seconds | Performance |

### Todos API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_todos | GET | Fetch all 200 todos | Positive |
| test_get_single_todo | GET | Fetch todo by ID | Positive |
| test_todo_has_required_fields | GET | Schema validation | Positive |
| test_completed_todos_exist | GET | Filter completed todos | Positive |
| test_incomplete_todos_exist | GET | Filter incomplete todos | Positive |
| test_invalid_todo | GET | Non-existent todo (404) | Negative |

---

## Key Features

- **All HTTP Methods** — GET, POST, PUT, DELETE covered
- **Status Code Validation** — 200, 201, 404 verified
- **JSON Schema Validation** — All required fields checked
- **Response Time Testing** — Performance under 2 seconds
- **Positive + Negative Tests** — Complete test coverage
- **Reusable APIClient** — Centralized base URL and methods
- **Auto CI/CD** — GitHub Actions on every push
- **HTML Reports** — Visual test results

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Internet connection
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/Sandeepvardhan-k/REST-API-Testing-Framework
cd REST-API-Testing-Framework

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all 19 tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html

# Run specific suite
pytest tests/test_posts.py -v
pytest tests/test_users.py -v
pytest tests/test_todos.py -v

# Run specific test
pytest tests/test_posts.py::TestPosts::test_get_all_posts -v
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:
Push code → GitHub Actions triggered
→ Ubuntu server starts
→ Python 3.9 installed
→ requests + pytest installed
→ All 19 tests run
→ HTML report saved
→ Pass/Fail shown on GitHub

Note: No Docker or Chrome needed —
API tests run directly with Python!

---

## Sample Test Output
tests/test_posts.py::TestPosts::test_get_all_posts    PASSED
tests/test_posts.py::TestPosts::test_get_single_post  PASSED
tests/test_posts.py::TestPosts::test_create_post      PASSED
tests/test_posts.py::TestPosts::test_update_post      PASSED
tests/test_posts.py::TestPosts::test_delete_post      PASSED
tests/test_posts.py::TestPosts::test_invalid_post     PASSED
tests/test_posts.py::TestPosts::test_response_time    PASSED
tests/test_users.py::TestUsers::test_get_all_users    PASSED
...
19 passed in 3.22s

---

## What I Validated
```python
# Status codes
assert response.status_code == 200   # GET success
assert response.status_code == 201   # POST created
assert response.status_code == 404   # Not found

# Schema validation
assert "id"     in data
assert "title"  in data
assert "body"   in data
assert "userId" in data

# Response time
assert response.elapsed.total_seconds() < 2

# Data validation
assert len(response.json()) == 100   # 100 posts
assert data["id"] == 1               # correct record
assert "@" in data["email"]          # valid email
```

---

## Requirements
requests
pytest
pytest-html

---

## Difference from UI Testing

| | Selenium Project | API Project |
|---|---|---|
| Tests | Frontend UI | Backend data |
| Tool | Selenium WebDriver | requests library |
| Speed | 30-60 seconds | Milliseconds |
| Browser | Chrome required | No browser |
| Focus | Visual elements | Data/Logic |

---

## Author

**Sandeepvardhan K**
- GitHub: [github.com/Sandeepvardhan-k](https://github.com/Sandeepvardhan-k)
- LinkedIn: # REST API Testing Framework

![Python](https://img.shields.io/badge/Python-3.9-blue)
![requests](https://img.shields.io/badge/requests-2.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen)
![Tests](https://img.shields.io/badge/Tests-19%20Passing-success)
![API](https://img.shields.io/badge/API-REST-blue)

Comprehensive REST API testing framework built with Python 
requests library and pytest. Tests JSONPlaceholder REST API 
covering all HTTP methods — GET, POST, PUT and DELETE — 
with status code validation, JSON schema verification 
and response time testing across 19 automated test cases.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Primary programming language |
| requests | HTTP library for API calls |
| pytest | Test framework and execution |
| pytest-html | HTML test report generation |
| GitHub Actions | CI/CD — auto runs tests on every push |

---

## Project Structure
api-testing-framework/
├── utils/
│   ├── init.py
│   └── api_client.py        # Reusable API helper class
├── tests/
│   ├── init.py
│   ├── test_posts.py        # Posts endpoint tests (7)
│   ├── test_users.py        # Users endpoint tests (6)
│   └── test_todos.py        # Todos endpoint tests (6)
├── reports/
│   └── report.html          # Generated HTML report
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions workflow
├── conftest.py
├── requirements.txt
└── .gitignore

---

## API Under Test

**JSONPlaceholder** — Free fake REST API for testing
Base URL: https://jsonplaceholder.typicode.com
Endpoints tested:
/posts    → Blog posts (100 records)
/users    → Users (10 records)
/todos    → Todo items (200 records)

---

## Test Cases (19 Total)

### Posts API — 7 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_posts | GET | Fetch all 100 posts | Positive |
| test_get_single_post | GET | Fetch post by ID | Positive |
| test_create_post | POST | Create new post | Positive |
| test_update_post | PUT | Update existing post | Positive |
| test_delete_post | DELETE | Delete a post | Positive |
| test_invalid_post | GET | Non-existent post (404) | Negative |
| test_response_time | GET | Response under 2 seconds | Performance |

### Users API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_users | GET | Fetch all 10 users | Positive |
| test_get_single_user | GET | Fetch user by ID | Positive |
| test_user_has_required_fields | GET | Schema validation | Positive |
| test_user_email_format | GET | Email contains @ | Positive |
| test_invalid_user | GET | Non-existent user (404) | Negative |
| test_user_response_time | GET | Response under 2 seconds | Performance |

### Todos API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_todos | GET | Fetch all 200 todos | Positive |
| test_get_single_todo | GET | Fetch todo by ID | Positive |
| test_todo_has_required_fields | GET | Schema validation | Positive |
| test_completed_todos_exist | GET | Filter completed todos | Positive |
| test_incomplete_todos_exist | GET | Filter incomplete todos | Positive |
| test_invalid_todo | GET | Non-existent todo (404) | Negative |

---

## Key Features

- **All HTTP Methods** — GET, POST, PUT, DELETE covered
- **Status Code Validation** — 200, 201, 404 verified
- **JSON Schema Validation** — All required fields checked
- **Response Time Testing** — Performance under 2 seconds
- **Positive + Negative Tests** — Complete test coverage
- **Reusable APIClient** — Centralized base URL and methods
- **Auto CI/CD** — GitHub Actions on every push
- **HTML Reports** — Visual test results

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Internet connection
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/Sandeepvardhan-k/REST-API-Testing-Framework
cd REST-API-Testing-Framework

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all 19 tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html

# Run specific suite
pytest tests/test_posts.py -v
pytest tests/test_users.py -v
pytest tests/test_todos.py -v

# Run specific test
pytest tests/test_posts.py::TestPosts::test_get_all_posts -v
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:
Push code → GitHub Actions triggered
→ Ubuntu server starts
→ Python 3.9 installed
→ requests + pytest installed
→ All 19 tests run
→ HTML report saved
→ Pass/Fail shown on GitHub

Note: No Docker or Chrome needed —
API tests run directly with Python!

---

## Sample Test Output
tests/test_posts.py::TestPosts::test_get_all_posts    PASSED
tests/test_posts.py::TestPosts::test_get_single_post  PASSED
tests/test_posts.py::TestPosts::test_create_post      PASSED
tests/test_posts.py::TestPosts::test_update_post      PASSED
tests/test_posts.py::TestPosts::test_delete_post      PASSED
tests/test_posts.py::TestPosts::test_invalid_post     PASSED
tests/test_posts.py::TestPosts::test_response_time    PASSED
tests/test_users.py::TestUsers::test_get_all_users    PASSED
...
19 passed in 3.22s

---

## What I Validated
```python
# Status codes
assert response.status_code == 200   # GET success
assert response.status_code == 201   # POST created
assert response.status_code == 404   # Not found

# Schema validation
assert "id"     in data
assert "title"  in data
assert "body"   in data
assert "userId" in data

# Response time
assert response.elapsed.total_seconds() < 2

# Data validation
assert len(response.json()) == 100   # 100 posts
assert data["id"] == 1               # correct record
assert "@" in data["email"]          # valid email
```

---

## Requirements
requests
pytest
pytest-html

---

## Difference from UI Testing

| | Selenium Project | API Project |
|---|---|---|
| Tests | Frontend UI | Backend data |
| Tool | Selenium WebDriver | requests library |
| Speed | 30-60 seconds | Milliseconds |
| Browser | Chrome required | No browser |
| Focus | Visual elements | Data/Logic |

---

## Author

**Sandeepvardhan K**
- GitHub: [github.com/Sandeepvardhan-k](https://github.com/Sandeepvardhan-k)
- LinkedIn: # REST API Testing Framework

![Python](https://img.shields.io/badge/Python-3.9-blue)
![requests](https://img.shields.io/badge/requests-2.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen)
![Tests](https://img.shields.io/badge/Tests-19%20Passing-success)
![API](https://img.shields.io/badge/API-REST-blue)

Comprehensive REST API testing framework built with Python 
requests library and pytest. Tests JSONPlaceholder REST API 
covering all HTTP methods — GET, POST, PUT and DELETE — 
with status code validation, JSON schema verification 
and response time testing across 19 automated test cases.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9 | Primary programming language |
| requests | HTTP library for API calls |
| pytest | Test framework and execution |
| pytest-html | HTML test report generation |
| GitHub Actions | CI/CD — auto runs tests on every push |

---

## Project Structure
api-testing-framework/
├── utils/
│   ├── init.py
│   └── api_client.py        # Reusable API helper class
├── tests/
│   ├── init.py
│   ├── test_posts.py        # Posts endpoint tests (7)
│   ├── test_users.py        # Users endpoint tests (6)
│   └── test_todos.py        # Todos endpoint tests (6)
├── reports/
│   └── report.html          # Generated HTML report
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions workflow
├── conftest.py
├── requirements.txt
└── .gitignore

---

## API Under Test

**JSONPlaceholder** — Free fake REST API for testing
Base URL: https://jsonplaceholder.typicode.com
Endpoints tested:
/posts    → Blog posts (100 records)
/users    → Users (10 records)
/todos    → Todo items (200 records)

---

## Test Cases (19 Total)

### Posts API — 7 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_posts | GET | Fetch all 100 posts | Positive |
| test_get_single_post | GET | Fetch post by ID | Positive |
| test_create_post | POST | Create new post | Positive |
| test_update_post | PUT | Update existing post | Positive |
| test_delete_post | DELETE | Delete a post | Positive |
| test_invalid_post | GET | Non-existent post (404) | Negative |
| test_response_time | GET | Response under 2 seconds | Performance |

### Users API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_users | GET | Fetch all 10 users | Positive |
| test_get_single_user | GET | Fetch user by ID | Positive |
| test_user_has_required_fields | GET | Schema validation | Positive |
| test_user_email_format | GET | Email contains @ | Positive |
| test_invalid_user | GET | Non-existent user (404) | Negative |
| test_user_response_time | GET | Response under 2 seconds | Performance |

### Todos API — 6 Tests
| Test | Method | Description | Type |
|------|--------|-------------|------|
| test_get_all_todos | GET | Fetch all 200 todos | Positive |
| test_get_single_todo | GET | Fetch todo by ID | Positive |
| test_todo_has_required_fields | GET | Schema validation | Positive |
| test_completed_todos_exist | GET | Filter completed todos | Positive |
| test_incomplete_todos_exist | GET | Filter incomplete todos | Positive |
| test_invalid_todo | GET | Non-existent todo (404) | Negative |

---

## Key Features

- **All HTTP Methods** — GET, POST, PUT, DELETE covered
- **Status Code Validation** — 200, 201, 404 verified
- **JSON Schema Validation** — All required fields checked
- **Response Time Testing** — Performance under 2 seconds
- **Positive + Negative Tests** — Complete test coverage
- **Reusable APIClient** — Centralized base URL and methods
- **Auto CI/CD** — GitHub Actions on every push
- **HTML Reports** — Visual test results

---

## How to Run Locally

### Prerequisites
- Python 3.9+
- Internet connection
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/Sandeepvardhan-k/REST-API-Testing-Framework
cd REST-API-Testing-Framework

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run Tests
```bash
# Run all 19 tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html

# Run specific suite
pytest tests/test_posts.py -v
pytest tests/test_users.py -v
pytest tests/test_todos.py -v

# Run specific test
pytest tests/test_posts.py::TestPosts::test_get_all_posts -v
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:
Push code → GitHub Actions triggered
→ Ubuntu server starts
→ Python 3.9 installed
→ requests + pytest installed
→ All 19 tests run
→ HTML report saved
→ Pass/Fail shown on GitHub

Note: No Docker or Chrome needed —
API tests run directly with Python!

---

## Sample Test Output
tests/test_posts.py::TestPosts::test_get_all_posts    PASSED
tests/test_posts.py::TestPosts::test_get_single_post  PASSED
tests/test_posts.py::TestPosts::test_create_post      PASSED
tests/test_posts.py::TestPosts::test_update_post      PASSED
tests/test_posts.py::TestPosts::test_delete_post      PASSED
tests/test_posts.py::TestPosts::test_invalid_post     PASSED
tests/test_posts.py::TestPosts::test_response_time    PASSED
tests/test_users.py::TestUsers::test_get_all_users    PASSED
...
19 passed in 3.22s

---

## What I Validated
```python
# Status codes
assert response.status_code == 200   # GET success
assert response.status_code == 201   # POST created
assert response.status_code == 404   # Not found

# Schema validation
assert "id"     in data
assert "title"  in data
assert "body"   in data
assert "userId" in data

# Response time
assert response.elapsed.total_seconds() < 2

# Data validation
assert len(response.json()) == 100   # 100 posts
assert data["id"] == 1               # correct record
assert "@" in data["email"]          # valid email
```

---

## Requirements
requests
pytest
pytest-html

---

## Difference from UI Testing

| | Selenium Project | API Project |
|---|---|---|
| Tests | Frontend UI | Backend data |
| Tool | Selenium WebDriver | requests library |
| Speed | 30-60 seconds | Milliseconds |
| Browser | Chrome required | No browser |
| Focus | Visual elements | Data/Logic |

---

## Author

**Sandeepvardhan K**
- GitHub: [github.com/Sandeepvardhan-k](https://github.com/Sandeepvardhan-k)
- LinkedIn:[https://linkedin.com/in/sandeep-vardhan-421b97339](https://www.linkedin.com/in/sandeep-vardhan-421b97339/)
- Email: sandeepvardhan9381@gmail.com
