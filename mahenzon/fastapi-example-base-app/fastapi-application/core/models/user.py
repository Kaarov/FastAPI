from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .base import Base
from .mixins.id_int_pk import IdIntPKMixin


class User(Base, IdIntPKMixin, SQLAlchemyBaseUserTable[int]):
    pass
