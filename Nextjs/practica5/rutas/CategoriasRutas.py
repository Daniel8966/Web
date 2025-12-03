from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select
from models.modelos import Categoria
from models.modelos import Categoria as CategoriaModelo
from schemas.librosEschema import  CategoriaBase , CategoriaBase, CategoriaRead
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión


router = APIRouter(
    prefix="/Categoria",
    tags=["Categoria"]
)


@router.post("/RegistrarCategoria", response_model=CategoriaRead)
def crear_Categoria(CategoriaBase: CategoriaBase, session: SessionDep ):
    nuevoCategoria = Categoria.from_orm(CategoriaBase)

    session.add(nuevoCategoria)
    session.commit()
    session.refresh(nuevoCategoria)
    return nuevoCategoria


@router.get("/TodosLosCategoriaes", response_model=list[CategoriaRead])
def listar_Categoriaes(session: SessionDep):
    Categoriaes = session.exec(select(Categoria)).all()
    return Categoriaes


@router.delete("/BorrarCategoria/{idCategoria}")
def borrar_Categoria_ID( idCategoria : int , session: SessionDep):
    # Buscar el libro
    statement = select(CategoriaModelo).where(CategoriaModelo.id == idCategoria)
    Categoria = session.exec(statement).first()

    if not Categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrado o eliminado previamente")
    # Eliminarlo
    session.delete(Categoria)
    session.commit()

    return {"mensaje": "Item con id "+str(idCategoria)+" eliminado correctamente"}



@router.patch("/actualizarCategoria/{idCategoria}")
def actuazlizar_Categoriaes_id( idCategoria : int , session: SessionDep , Categoria_editado : CategoriaBase):
    # Buscar el libro
    statement = select(CategoriaModelo).where(CategoriaModelo.id == idCategoria)
    Categoria = session.exec(statement).first()

    if not Categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    
    
    if Categoria_editado.descripcion is not None:
        Categoria.descripcion = Categoria_editado.descripcion

    session.commit()
    session.refresh(Categoria)
    return Categoria