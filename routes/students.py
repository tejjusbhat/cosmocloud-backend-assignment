from fastapi import APIRouter, HTTPException
from models.student import StudentCreate, StudentOut, StudentUpdate
from db.mongodb import students_collection
from typing import Optional
from bson import ObjectId
from fastapi.responses import JSONResponse
from fastapi import Response
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()

# Helper function to convert ObjectId to string
def convert_id(obj):
    obj["id"] = str(obj["_id"])
    del obj["_id"]
    return obj

# MongoDB client and collection setup
mongo_uri = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(mongo_uri)
db = client["student_management"]
students_collection = db["students"]

# Routes definition
@router.post("/students", response_model=StudentOut, status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student in the database.
    """
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    student_dict["id"] = str(result.inserted_id)
    return student_dict

@router.get("/students", response_model=dict)
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    """
    List students with optional filters for country and age.
    """
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = []
    async for student in students_collection.find(query):
        students.append(convert_id(student))
    
    return {"data": students}

@router.get("/students/{id}", response_model=StudentOut)
async def fetch_student(id: str):
    """
    Fetch a single student by their ID.
    """
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return convert_id(student)

@router.patch("/students/{id}", response_model=None, status_code=204)
async def update_student(id: str, student: StudentUpdate):
    """
    Update a student's information by their ID.
    """
    update_data = {k: v for k, v in student.dict(exclude_unset=True).items()}
    if update_data:
        result = await students_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": update_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")

    return Response(status_code=204)

@router.delete("/students/{id}", response_model=None, status_code=200)
async def delete_student(id: str):
    """
    Delete a student by their ID.
    """
    result = await students_collection.delete_one({"_id": ObjectId(id)})  # Async delete
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return JSONResponse(status_code=200, content={"message": "Student deleted successfully"})
