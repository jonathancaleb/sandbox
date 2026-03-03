from fastapi import FastAPI

app = FastAPI()

@app.get("/expenses")
def read_data():
    return [ {"id": 1, "description": "coffee", "amount": 5}, {"id": 1, "description": "coffee", "amount": 5}  ]