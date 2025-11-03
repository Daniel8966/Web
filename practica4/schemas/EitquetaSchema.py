from pydantic import BaseModel

class EtiquetaBase(BaseModel):
    descripcion: str


class EtiquetaCreate(EtiquetaBase):
    pass


class EtiquetaRead(EtiquetaBase):
    id: int

    class Config:
        from_attributes = True  
