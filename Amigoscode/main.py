from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(id=uuid4(), 
        first_name="Leo", 
        last_name="Messi",
        middle_name="Leonardo",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(id=uuid4(), 
        first_name="Meerim", 
        last_name="Alymova",
        middle_name="Meerik",
        gender=Gender.female,
        roles=[Role.student]
    )
]

@app.get("/")
def root():
    return {""}

@app.get("/api/v1/users")
async def fetch_users():
    return db;


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists!"
    )