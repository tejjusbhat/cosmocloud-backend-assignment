from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.students import router as students_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students_router)
