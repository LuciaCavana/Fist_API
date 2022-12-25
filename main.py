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


id_person = {
    1:{
        "name":"Lucia", 
        "age":22
        },
    2:{
        "name":"Matias",
        "age":17
        },
    3:{
        "name":"Fernando", 
        "age":40
        },
    4:{
        "name":"Martina", 
        "age":20
        },
    5:{
        "name":"Lucila", 
        "age":50
        },
}

app = FastAPI()

@app.get(
    path="/", 
    status_code=status.HTTP_200_OK,
    tags=["Home"])
def home():
    
    return {"Hello": "Word"}

# Request  and Response Body
@app.post(
    path="/person/new",
    response_model=PersonOut, 
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person in the app")
def Create_Person(person: Person = Body(...)):
    """
    Create Person

    This path operation creates a person in the app and save the information in the database

    Parameters: 
    - Request body parameter: 
        - **person: Person** -> A person model with first name, last name, age, hair color, marital stauts, email and earnings

    Returns a person model with first name, last name, age, hair color and marital status
    """
    return person

#Validaciones Querry parameters 
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Details person in the app",
    deprecated=True)
def show_person(    
    name:str= Query(..., 
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
    
    
    """
    Show Person

    This path operation shows the name and age of the people that are saved in the database

    Parameters: 
    - Request body parameter: 
        - **name: Optional[str]** -> the name of the person
        - **age:int** -> the age of the person

    Returns name and age of people
    """
    return {name:age}
#Validaciones: Path Parameters
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="show a person exist") 
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title='Id de la persona',
        description= 'Ingresa el id de la persona buscada. Es un campo obliatorio',
        example=1
        ) 
    ):
    '''
    Show Person
    
    This path operation proves that a person's id exists in the data base and shows the name and age
    
    Parameters: 
    - Request path parameter: 
        - **person_id: int** -> the id of a person

    Returns if a person exists, the name and age or an HTTP error if the person does not exist in the database
    '''
    if person_id not in id_person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "¡This person doesn't exist!"
        )
    date =  dict(id_person[person_id])
    return {person_id:"It Exists!",date["name"]:date["age"]}


#Validaciones: Request Body
@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Update person in the database")
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
    '''
    Update Person

    This path operation modify the information of a person and their location in the database
    
    Parameters: 
    - Request body parameter: 
        - **person:Person** -> A person model with first name, last name, age, hair color, marital stauts, email and earnings
        - **location:Location** -> A location model with city, state and country 
    - Request path parameter:
        - **person_id: int** -> Person id to modify

    Returns the person with the modified fields or an HTTP error message 
    '''
    if person_id not in id_person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exist! Could not be modified!"
        )
    results = person.dict()
    results.update(location.dict())
    return results

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    summary="Login to the app"
    )
def login(username:str= Form(...), password:str=Form(...)):
    '''
    Login

    This path operation enter a section with a user previously registered in the app and saved in the database

    Parameters:
        - Request form parameter:
            - **username:str** -> username entered in the person model 
            - **password** -> password entered in the person model

    Return the username and success message
    '''
    return LoginOut(username=username)


#Cookies and Header class
@app.post("/contact",tags=["Server"],summary="")
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
    '''
    Contact 
    
    This path operation the user enters his data and a message to send to the owner of the app

    Parameters:
        - Request form parameter:
            - **first_name:str** -> person's first name
            - **last_name** -> person's last name
            - **email:Emailstr** -> person's email
            - **message:str** -> message you want to send
        - Request header parameter:
            - **user_agent:Optional[str]** -> header obtained from the person's visit   
        -Request cookie parameter:
            - **ads:Optional[str]** -> cookie obtained from the person's visitis
    
    Return the header obtained from the person
    '''
    return user_agent 

#Files
@app.post(
    path="/post-image",
    tags=["Files"],
    summary="Upload files"
)
def post_image(
    image: UploadFile = File(...)
):
    '''
    Post image

    This path operation allows you to post an image in the app to the database.

    Parameters:
    - Request body parameter:
        - **image: UploadFile** -> This is the image to upload. It's required.

    Returns a JSON with the image's name, format and size in kb.
    '''
    return {
        "Filename":image.filename,
        "Format":image.content_type,
        "Size(kb)":round(len(image.file.read())/1024,ndigits=2) 
    }
    
