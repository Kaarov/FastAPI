from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
