from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/")
def create(dept: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, dept.name)

@router.get("/")
def all(db: Session = Depends(get_db)):
    return crud.get_departments(db)