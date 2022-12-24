from typing import Optional
from pydantic import BaseModel
from pydantic import Field, EmailStr, PositiveFloat

class Person(BaseModel):
    person_id:int=Field()
    first_name
    last_name
    age
    is_married
    hair_color
    person_email
    earnings
    
    
    
    
    
    
    
    city:str = Field(...,max_length=50, min_length=1, title="City name", description="This is city name") 
    state: str = Field(...,max_length=50, min_length=1, title="State name", description="This is state name")
    country: str = Field(...,max_length=50, min_length=1, title="Country name", description="This is country name")
    class Config:
        schema_extra={
            "example":{
                "city":"Saavedra",
                "state":"CABA",
                "country":"Argentina"
            }
        }