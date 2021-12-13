from typing import Optional
from pydantic import BaseModel, EmailStr, Field


#Create User Profile Schema
class UserSchema(BaseModel):
    fullname: str = Field(..., max_length = 50, example="Joe Dirt")
   
class PrivateUserSchema(UserSchema):
    height: float = Field(...)
    age: float = Field(...)
    weight: float = Field(...)
    email: EmailStr = Field(...)

class CreateUserSchema(PrivateUserSchema):
    password: str = Field(..., min_length = 6, example="supersecurepassword")

class PriviligedUserSchema(CreateUserSchema):
    user_type: Optional[int]

#Search Schemas
class SearchUserSchema(BaseModel):
    fullname: str = Field(..., max_length = 50, example="Joe Dirt")
    height: Optional[float]
    age: Optional[float]
    weight: Optional[float]
    email: Optional[EmailStr]

#Login Schemas
class LoginUserSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserSearchSchema(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=255, example="Cool Name")
    id: Optional[int] = Field(gt=0, lt=2147483647, example=6587)
    age: Optional[int] = Field(gt=0, lt=1000, example=23)
    email: Optional[EmailStr] = Field(example="JimboJohnson@Ultracorp.io")
    job: Optional[str] = Field(min_length=2, max_length=255, example="Dirt Inspector")
    phone_number: Optional[str] = Field(min_length=2, max_length=32, example="245-143-4678")
    user_type: Optional[int] = Field(gt=0, lt=1000, example=3)
    schedule: Optional[list]

# User Update Schemas

