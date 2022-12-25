#Python
from typing import Optional

#from Generate_Models import person

#Models
from Models.Person import Person, PersonOut
from Models.Location import Location
from Models.Login import LoginOut

#Pydantic
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Cookie, Header, File, UploadFile

id_person = [1,2,3,4,5]

app = FastAPI()

@app.get(
    path="/", 
    status_code=status.HTTP_200_OK)
def home():
    
    return {"Hello": "Word"}

# Request  and Response Body
@app.post(
    path="/person/new",
    response_model=PersonOut, 
    status_code=status.HTTP_201_CREATED)
def Create_Person(person: Person = Body(...)):
    
    return person

#Validaciones Querry parameters 
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK)
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
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK) 
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title='Id de la persona',
        description= 'Ingresa el id de la persona buscada. Es un campo obliatorio',
        example=1
        )
    ):
    if person_id not in id_person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "¡This person doesn't exist!"
        )
    return {person_id:"It Exists!"}

#Validaciones: Request Body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_201_CREATED)
def update_person(
    person_id: int = Path(
        ...,
        description= "Este es el ID de la persona",
        title="ID de la persona",
        gt = 0,
        example=1
    ),
    person:Person = Body(...),
    location: Location = Body(...) 
):
    results = person.dict()
    results.update(location.dict())
    return results

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
    )
def login(username:str= Form(...), password:str=Form(...)):
    
    return LoginOut(username=username)


#Cookies and Header class
@app.post("/contact")
def contact(
    first_name:str=Form(
        ...,
        max_length=20,
        min_length=1
        ),
    last_name:str=Form(
        ...,
        max_length=20,
        min_length=1
        ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str]=Header(default=None),
    ads:Optional[str]=Cookie(default=None)
):
    return user_agent 

#Files
@app.post(
    path="/post-image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename":image.filename,
        "Format":image.content_type,
        "Size(kb)":round(len(image.file.read())/1024,ndigits=2) 
    }
    pass
