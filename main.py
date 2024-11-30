from fastapi import FastAPI
from routes.students import router as students_router

app = FastAPI()

app.include_router(students_router)
