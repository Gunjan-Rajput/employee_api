from models import Employee, Department, User
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from auth import hash_password, verify_password


# ---------------- DEPARTMENT ----------------

def create_department(db: Session, name: str):
    dept = Department(name=name)
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept


def get_departments(db: Session):
    return db.query(Department).all()


# ---------------- EMPLOYEE ----------------

def create_employee(db: Session, data):
    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def get_employees(
    db: Session,
    name=None,
    department=None,
    page=1,
    limit=5,
    sort_by="id",
    order="asc"
):

    query = db.query(Employee)

    if name:
        query = query.filter(
            Employee.name.ilike(f"%{name}%")
        )

    if department:
        query = query.join(Department).filter(
            Department.name.ilike(f"%{department}%")
        )

    if hasattr(Employee, sort_by):

        column = getattr(Employee, sort_by)

        if order.lower() == "desc":
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))

    offset = (page - 1) * limit

    return query.offset(offset).limit(limit).all()


def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(
        Employee.id == emp_id
    ).first()


def delete_employee(db: Session, emp_id: int):

    emp = get_employee(db, emp_id)

    if emp:
        db.delete(emp)
        db.commit()

    return emp


# ---------------- USER ----------------

def create_user(db: Session, user):

    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_username(db: Session, username: str):

    return db.query(User).filter(
        User.username == username
    ).first()


def get_user_by_email(db: Session, email: str):

    return db.query(User).filter(
        User.email == email
    ).first()


def login_user(db: Session, email: str, password: str):

    user = get_user_by_email(db, email)

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user