from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
import crud
import schemas

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/")
def create(
    emp: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, emp)


@router.get("/")
def all(
    name: Optional[str] = None,
    department: Optional[str] = None,
    page: int = 1,
    limit: int = 5,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):

    return crud.get_employees(
        db=db,
        name=name,
        department=department,
        page=page,
        limit=limit,
        sort_by=sort_by,
        order=order
    )


@router.get("/{emp_id}")
def get(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_employee(db, emp_id)


@router.delete("/{emp_id}")
def delete(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_employee(db, emp_id)