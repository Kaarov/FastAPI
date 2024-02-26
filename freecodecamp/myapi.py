from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name": "Onya",
        "age": 20,
        "year": "2021"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"welcome": "Hi!"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The Id of the student that you want to see"), gt=0, lt=3):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")

# @app.get("/get-by-name/{student_id}")
# def get_student(*, student_id: int, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists!"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exists!"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/")
def delete_student(student_id: int = Query(None, description="The Id of the student that you want to see")):
    if student_id not in students:
        return {"Error": "Student does not exists!"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully!"}