from pydantic import BaseModel

class EnvioBase(BaseModel):
    descripcion: str

class EnvioRead(EnvioBase):
    id: int

    class Config:
        from_attributes = True  
