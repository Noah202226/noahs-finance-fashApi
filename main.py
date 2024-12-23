from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    qty: int

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test 2"}

@app.post("/add-item/{item_id}")
def add_item(item_id: int, item: Item):
    return {f"Item {item_id}",f"{item.name} :Added."}


# ASGI adapter
handler = Mangum(app)