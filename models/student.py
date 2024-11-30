from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Address(BaseModel):
    city: str
    country: str

class StudentBase(BaseModel):
    name: str
    age: int
    address: Address

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]

class StudentOut(StudentBase):
    id: str  # Return 'id' instead of '_id' for MongoDB documents

    class Config:
        # Convert MongoDB ObjectId to string in JSON responses
        json_encoders = {
            ObjectId: str
        }
