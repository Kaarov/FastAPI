from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = FastAPI()

engine = create_async_engine("sqlite+aiosqlite:///books.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]


class Base(DeclarativeBase):
    pass


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]


@app.post("/setup_database")
async def setup_database() -> dict[str, str]:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    return {"message": "Database setup complete"}


class BookAddSchema(BaseModel):
    title: str
    author: str


class BookSchema(BookAddSchema):
    id: int


@app.post("/books")
async def add_book(book: BookAddSchema, session: SessionDep) -> dict[str, str]:
    new_book = BookModel(
        title=book.title,
        author=book.author,
    )
    session.add(new_book)
    await session.commit()
    return {"message": "Book added"}


@app.get("/books")
async def get_book(session: SessionDep) -> list[BookSchema]:
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()
