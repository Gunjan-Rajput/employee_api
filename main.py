from fastapi import FastAPI

from database import Base, engine

import models

from routers import employee
from routers import department
from routers import auth_router

app = FastAPI(
    title="Employee Management System"
)

Base.metadata.create_all(bind=engine)

app.include_router(employee.router)

app.include_router(department.router)

app.include_router(auth_router.router)


@app.get("/")
def home():

    return {

        "message": "FastAPI Employee API Running"

    }