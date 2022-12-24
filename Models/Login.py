from pydantic import BaseModel, Field

class LoginOut(BaseModel):
    username:str=Field(..., max_length=20, min_length=1, example="Lucia123", title="Username", description="This is your Username")
    mensage:str=Field(default="Login Succesfully!")