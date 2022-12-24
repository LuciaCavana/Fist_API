#Python
from typing import Optional

#Models
from Models import Person, Location

#Pydantic
#from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

@app.get("/")
def home():
    
    return {"Hello": "Word"}

# Request  and Response Body
@app.post("/person/new")
def Create_Person(person: Person.Person = Body(...)):
    return person

#Validaciones Querry parameters 
@app.get("/person/detail")
def show_person(    
    name:Optional[str] = Query(
        default=None, 
        min_length=1, 
        max_length=30,
        title='Tu nombre', 
        description= 'Ingresa tu nombre. Tiene entre 1 a 50 caracteres', #No obligatorio
        example="Lucia"
        ), 
    age: int = Query(
        ..., 
        ge=18,
        title="Edad", 
        description="Ingresa tu edad. Es un campo obligatorio", #obligatorio
        example=22
        ) 
    ):  
    return {name:age}

#Validaciones: Path Parameters
@app.get("/person/detail/{person_id}") 
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title='Id de la persona',
        description= 'Ingresa el id de la persona buscada. Es un campo obliatorio',
        example=1
        )
    ):
    return {person_id:"It Exists!"}

#Validaciones: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="ID de la persona",
        description= "Este es el ID de la persona",
        gt = 0,
        example=1
    ),
    person:Person.Person = Body(...),
    location: Location.Location = Body(...) 
):
    results = person.dict()
    results.update(location.dict())
    return results


