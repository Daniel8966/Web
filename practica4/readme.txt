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
├── models                 # Modelos de la base de datos
├── schemas                # Pydantic models (ItemCreate, etc.)
├── database               # Configuración de la base de datos
└── routes                 # Routeo para cada endpoint de la app