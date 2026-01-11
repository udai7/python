from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    origin: str

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "These are the items"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    return {"error": "Item not found"}
