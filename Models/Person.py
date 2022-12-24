from typing import Optional
from .HairColor import HairColor as HC
from pydantic import BaseModel
from pydantic import Field, EmailStr, PositiveFloat

class PersonBase(BaseModel):
    person_id:int=Field(..., ge=0,title="Person ID", description="This is Person ID")
    first_name:str=Field(..., max_length=30, min_length=1, title="First name", description="This is the person first name")
    last_name:str=Field(..., max_length=30, min_length=1, title="Last name", description="This is the person last name")
    age: int = Field(..., gt=1, lt=115, title="Person age", description="This is person age")
    is_married:bool=Field(default=None, title="", description="")
    hair_color: Optional[HC]=Field(default=None, title="Person hair color", description="This is person hair color")
    person_email: EmailStr = Field(default=None, title="Person email", description="This is person email")
    earnings: PositiveFloat = Field(default=None, title="Person earnings", description="This is person earnings")




#Generate Person
class Person(PersonBase):
    password: str=Field(...,max_length=16,min_length=8, title="Passwor", description="This Password requires a minimum of 8 characters and maximum of 16")
    class Config:
        schema_extra={
            "example":{
                "person_id": "1",
                "first_name": "Lucia",
                "last_name": "Cavana",
                "age": 22,
                "hair_color": "brown",
                "is_married": False,
                "person_email": "luciacavana@yahoo.com",
                "earnings": 120000,
                "password":"admin123"
            }
        }


#Person Out
class PersonOut(PersonBase):
    pass 