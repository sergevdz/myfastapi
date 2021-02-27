from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
# from datetime import datetime
#datetime.now().hour

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def red_root():
    return {"asd": "asdasd"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_prime": item.price, "item_id": item_id}

