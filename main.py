from fastapi import FastAPI, HTTPException
from database import get_connection, create_tables
from models import Expense

app = FastAPI(title="Expense Tracker API")

create_tables()

@app.post("/expenses")
def add_expense(expense: Expense):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (title, amount, category, type, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (expense.title, expense.amount, expense.category, expense.type, expense.date))
    conn.commit()
    conn.close()
    return {"message": "Transaction added successfully!"}

@app.get("/expenses")
def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/expenses/category/{category}")
def get_by_category(category: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="No transactions found for this category")
    return [dict(row) for row in rows]

@app.get("/expenses/summary/{month}")
def get_summary(month: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT type, SUM(amount) as total
        FROM expenses
        WHERE date LIKE ?
        GROUP BY type
    ''', (f"{month}%",))
    rows = cursor.fetchall()
    conn.close()
    summary = {row["type"]: row["total"] for row in rows}
    income = summary.get("income", 0)
    expense = summary.get("expense", 0)
    return {
        "month": month,
        "total_income": income,
        "total_expense": expense,
        "net_savings": income - expense
    }

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    return {"message": f"Transaction {expense_id} deleted successfully!"}