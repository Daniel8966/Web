### Aqui pondre la estructura de todo el documento 

--- 
Objetivo: Hacer un CRUD con fast api para una libreria 

Entidades para endpoints con crud 
    Libro
    Autores
    Editorial
    Categorias 
    Formato(1,0)
    Publico Objetivo


endpoints con informacion adicional 
    libros del mismo autor 
    libros por categoria 
    libros por serie 
    libros por publico Objetivo

Paginacion  
    skip: limit 

todo a tra vez de query parameters 

No eliminar en cascada para categorias o libros 

Modelado de la base de datos 

Libro: 
    ID int primary key
    ISBN VARCHAR 
    TITULO VARCHAR 
    Autores - > m : m - > Catalogo de Autores 
    Editorial -> 1 : m -> Catalogo de Editoriales 
    Ano de publicacion DATE 
    paginas int 
    Categorias ->  m : m -> Categorias 
    Precio float 
    Formato (Digital o fisico 1 o 0 ) 
    Publico Objetivo -> 1 :  m ->  Catalogo 
    Serie -> 1 : m -> C. series 

Libro_tiene_autores:
    idLibro
    idAutores

Libro_tiene_categoria:
    idLibro
    idCategoria

Autor: 
    id Autor
    nombre 

(Catalogo)
Editorial: 
    id Editorial
    nombre
    Direccion

(Catalogo)
Categoria:
    id
    descripcion

(Catalogo):
Publico Objetivo:
    id
    descripcion

(Catalogo)
Serie :
    id
    numeroDeSerie
    descripcion serie 

1 libro solo tiene un publico objetivo 
1 libro solo tiene una editorial 
