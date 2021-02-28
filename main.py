from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
# from datetime import datetime
#datetime.now().hour

app = FastAPI()
fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def red_root():
    return {"asd": "asdasd"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
           {"description": "Long description"} 
        )
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_prime": item.price, "item_id": item_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
           {"description": "Long description"} 
        )
    return item

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({price_with_tax: "price_with_tax"})
    return item
