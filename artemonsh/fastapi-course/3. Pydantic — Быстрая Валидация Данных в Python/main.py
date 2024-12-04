from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict


app = FastAPI()

data = {
    "email": "abc@gmail.ru",
    "bio": "I like cupcakes!",
    "age": 12,
}

data_wo_age = {
    "email": "abc@gmail.ru",
    "bio": "I like cupcakes!",
    # "gender": "male",
    # "birthday": "2002"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)

    model_config = ConfigDict(extra="forbid")


users = []


@app.post("/users")
def add_user(user: UserSchema) -> dict:
    users.append(user)
    return {"status": "ok", "message": "user added"}


@app.get("/users")
def add_user() -> list[UserSchema]:
    return users


# class UserAge(UserSchema):
#     age: int = Field(ge=0, le=130)


# print(repr(UserSchema(**data_wo_age)))
# print(repr(UserAge(**data)))
