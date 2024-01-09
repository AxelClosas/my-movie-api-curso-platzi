# Clase Método POST en FastAPI, se integra la clase Body
# Validación de parametros de Ruta utilizando Path
# Validación de parametros Query utilizando Query
from fastapi import FastAPI, status

# Importamos la clase BaseModel que nos permitirá crear los esquemas
# Validación de tipos de datos usando Field
from fastapi.responses import HTMLResponse

# Importamos la función para crear el token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

# Routers
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi API de Peliculas"
app.version = "0.0.1"

# Llamamos el Middleware para que se ejecute con el inicio de la aplicación
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)


# Listado de peliculas
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Terror",
    },
]


# Ruta principal
@app.get("/", tags=["home"])
def index():
    return HTMLResponse("<h1>Hola mundo!<h1>")
