# FastAPI Calculator - Assignment 8

## Project Description

This project is a FastAPI calculator application that performs basic mathematical operations through a web interface and API endpoints. The calculator supports addition, subtraction, multiplication, and division.

The project also includes unit tests, integration tests, and an end-to-end test using Playwright. Docker is used to containerize the application, and GitHub Actions is used for continuous integration and automated testing.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pytest
- Playwright
- Docker
- GitHub Actions
- HTML

## Calculator Operations

The calculator supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero validation

## Running the Application

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

Open the application in your browser:

```text
http://localhost:8000
```

## Running the Tests

Run the unit tests:

```bash
python -m pytest tests/unit -v
```

Run the integration tests:

```bash
python -m pytest tests/integration -v
```

Run the end-to-end test:

```bash
python -m pytest tests/e2e -v
```

## Docker

Build the Docker image:

```bash
docker build -t fastapi-calculator .
```

Run the Docker container:

```bash
docker run --name fastapi-calculator-container -p 8000:8000 fastapi-calculator
```

The application can then be accessed at:

```text
http://localhost:8000
```

## Automated Testing

GitHub Actions automatically runs the project tests when code is pushed to the repository. The CI workflow installs the required dependencies and Playwright Chromium, starts the FastAPI application, and runs the unit, integration, and end-to-end tests.