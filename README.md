# Expense Tracker API

A RESTful API built with FastAPI and SQLite supporting full CRUD operations, category filtering, and monthly income and expense summary reporting.

## Features

- Add income and expense transactions
- Retrieve all transactions
- Filter transactions by category
- Get monthly summary showing total income, total expenses, and net savings
- Delete transactions by ID

## Tech Stack

- **Python** - Core programming language
- **FastAPI** - REST API framework
- **SQLite** - Lightweight database for storing transactions
- **Uvicorn** - ASGI server to run the application
- **Pydantic** - Data validation and schema modeling

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/AdapakaGunaSekhar004/Expense-Tracker-API.git
cd Expense-Tracker-API
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the application:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /expenses | Add a new transaction |
| GET | /expenses | Get all transactions |
| GET | /expenses/category/{category} | Get transactions by category |
| GET | /expenses/summary/{month} | Get monthly income/expense summary |
| DELETE | /expenses/{expense_id} | Delete a transaction by ID |

## Example Request

Add a transaction:

```json
{
  "title": "Salary",
  "amount": 25000.0,
  "category": "salary",
  "type": "income",
  "date": "2026-03-01"
}
```

Example summary response for March 2026:

```json
{
  "month": "2026-03",
  "total_income": 25000.0,
  "total_expense": 8150.0,
  "net_savings": 16850.0
}
```

## Project Structure

```
Expense-Tracker-API/
├── main.py         # API routes and endpoints
├── database.py     # Database connection and table creation
├── models.py       # Pydantic data models
└── README.md       # Project documentation
```

## Key Concepts Demonstrated

- RESTful API design with FastAPI
- CRUD operations (Create, Read, Delete)
- SQLite database integration with Python
- Data validation using Pydantic models
- Interactive API documentation via Swagger UI