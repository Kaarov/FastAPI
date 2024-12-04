from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="Home page", tags=["Homa Tags"])
def home():
    return "Hello World"


# === 1 способ ===
# fastapi dev main.py

# === 2 способ ===
# uvicorn main:app --reload

# === 3 способ ===
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
