from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserRead(schemas.BaseModel[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
