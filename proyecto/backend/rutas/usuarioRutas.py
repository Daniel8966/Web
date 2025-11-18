from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlmodel import Session, select, delete
from models.models import Usuario 
from schemas.usuarioSchema import UsuarioCreate, UsuarioPublico, UsuarioLogin
from database.SessionDep import SessionDep  # tu dependencia para obtener la sesión



router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.get("/", )
def obtenerUsuarios(session: SessionDep):
    autores = session.exec(select(Usuario)).all()
    if not autores:
        raise HTTPException(status_code=404, detail="usuarios  no encontrado o eliminados previamente")
    return autores

@router.post("/")
def registrarUsuario(usuario: UsuarioCreate, session: SessionDep):

    nuevoUsuario = Usuario(**usuario.model_dump())

    session.add(nuevoUsuario)
    session.commit()
    session.refresh(nuevoUsuario)

    return {"mensaje": "Usuario registrado exitosamente", "usuario": nuevoUsuario}

@router.delete("/usuarios/eliminar-todos")
def eliminar_todos_los_usuarios(session: SessionDep):

    session.exec(delete(Usuario))   # ← Borra todos los registros de la tabla
    session.commit()

    return {"mensaje": "Todos los usuarios fueron eliminados"}


@router.post("/login", )
def iniciar_sesion(session: SessionDep, usuario: UsuarioLogin):
    Comprobarusuario = session.exec(select(Usuario).where(
        Usuario.nombre == usuario.nombre,
        Usuario.password == usuario.password)).first()

    if not Comprobarusuario:
        raise HTTPException(status_code=404, detail="usuarios  no encontrado o eliminados previamente")
    
    return {"mensaje": "Login exitoso", "usuario": Comprobarusuario}
