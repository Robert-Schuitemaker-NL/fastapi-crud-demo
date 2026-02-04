from fastapi import FastAPI, HTTPException, Query
from sqlmodel import Session, select

from app.db import engine, init_db
from app.models import Item
from app.schemas import ItemCreate, ItemUpdate

app = FastAPI(title="CRUD Demo API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items", status_code=201)
def create_item(payload: ItemCreate):
    item = Item(name=payload.name, description=payload.description)
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items")
def list_items(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    q: str | None = None,
):
    with Session(engine) as session:
        stmt = select(Item)
        if q:
            stmt = stmt.where(Item.name.contains(q))
        stmt = stmt.offset(offset).limit(limit)
        items = session.exec(stmt).all()
        return {"limit": limit, "offset": offset, "count": len(items), "items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

@app.put("/items/{item_id}")
def replace_item(item_id: int, payload: ItemCreate):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        item.name = payload.name
        item.description = payload.description
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.patch("/items/{item_id}")
def update_item(item_id: int, payload: ItemUpdate):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(item, k, v)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return None
