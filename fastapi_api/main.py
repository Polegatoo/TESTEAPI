from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha Primeira API", version="1.0.0")

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"message": "API online! Use /docs para ver a documentação."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item):
    return {"created": item}
