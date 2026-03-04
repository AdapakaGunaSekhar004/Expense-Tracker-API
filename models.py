from pydantic import BaseModel

class Expense(BaseModel):
    title: str
    amount: float
    category: str
    type: str   # "income" or "expense"
    date: str   # format: YYYY-MM-DD