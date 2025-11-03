WWAAAA 
aqui voy aponer el esqueleto del proyecto 

REQUISITOS 

# Modelos en papel 
# ITEM: idItem , peso, ganancia, categorias (etiquetas), EnvioFInal|=Null 
# ETIQUETAS: idEtiqueta, descripcion
# items_tiene_etiquetas: idItem, idEtiqueta
# Envio: idEnvio , destino, itemsPorEnviar



ESTRUCTURA 

practica4/
│
├── main.py                # Punto de entrada (inicia FastAPI)
├── models.py              # Modelos de la base de datos
├── schemas.py             # Pydantic models (ItemCreate, etc.)
├── database.py            # Configuración de la base de datos
└── routes/
    └── items.py           # Aquí guardas tus rutas relacionadas con items