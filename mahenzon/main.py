from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {"msg": "Hello index!"}


@app.get("/items/")
def list_items():
    return [
        "item1",
        "item2",
        "item3"
    ]


@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return f"Hello {name}"


@app.post("/users")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
