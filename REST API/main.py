from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class expense(BaseModel):
    id: int
    item: str
    price: float



expenses = []

@app.get("/expenses")
def read_data():
    return expenses

@app.post("/update")
def create_data(expense: expense):
    print(expense)
    expenses.append(expense)
    return
