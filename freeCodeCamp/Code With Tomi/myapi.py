from typing import Optional

from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    }
}


@app.get("/")
def index():
    return {"name": "First Name"}


@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student_by_name(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"msg": "Student not found"}
