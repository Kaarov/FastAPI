import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Асинхронность в Python",
        "author": "Стен",
    },
    {
        "id": 2,
        "title": "Backend разработка в Python",
        "author": "Макс"
    },
]


@app.get(
    "/books",
    tags=["Книги 📚"],
    summary="Получить все книги",
)
def read_books() -> list[dict]:
    return books


@app.get(
    "/books/{book_id}",
    tags=["Книги 📚"],
    summary="Получить конкретную книжку",
)
def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдено!")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books", tags=["Книги 📚"])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Книга успешно добавлена"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
