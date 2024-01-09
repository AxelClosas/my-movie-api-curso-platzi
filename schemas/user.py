from pydantic import BaseModel


# Creamos la clase User
class User(BaseModel):
    email: str
    password: str
