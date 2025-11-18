from typing import Optional
from sqlmodel import SQLModel


from sqlmodel import SQLModel

class UsuarioLogin(SQLModel):
    nombre: str
    password: str

    
class UsuarioCreate(SQLModel):
    nombre: str
    password: str

class UsuarioPublico(SQLModel):
    id: int
    nombre: str
