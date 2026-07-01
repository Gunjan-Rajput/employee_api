from pydantic import BaseModel, EmailStr


# ---------------- Department ----------------

class DepartmentCreate(BaseModel):
    name: str


class DepartmentOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# ---------------- Employee ----------------

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    age: int
    salary: int
    department_id: int


class EmployeeOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    age: int
    salary: int
    department_id: int

    class Config:
        from_attributes = True


# ---------------- User ----------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str