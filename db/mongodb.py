from motor.motor_asyncio import AsyncIOMotorClient
import os

mongo_uri = os.getenv("MONGO_URI")

# MongoDB client
client = AsyncIOMotorClient(mongo_uri)
db = client["student_management"]
students_collection = db["students"]
