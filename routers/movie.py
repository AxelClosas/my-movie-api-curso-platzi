from fastapi import APIRouter

# Clase Método POST en FastAPI, se integra la clase Body
# Validación de parametros de Ruta utilizando Path
# Validación de parametros Query utilizando Query
from fastapi import Path, Query, status, Depends

# Importamos la clase BaseModel que nos permitirá crear los esquemas
# Validación de tipos de datos usando Field
from fastapi.responses import JSONResponse

# Importamos la clase Optiona desde typing para agregar un valor como opcional dentro de nuestro esquema
from typing import Optional, List

# Importamos la función para crear el token
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

from middlewares.jwt_bearer import JWTBearer

# Importamos el servicio de Movies
from services.movie import MovieService

# Importamos Schema Movie
from schemas.movie import Movie

movie_router = APIRouter()


# Ruta de acceso /movies
@movie_router.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(
        content=jsonable_encoder(result), status_code=status.HTTP_200_OK
    )


# Ruta de acceso con parametro de ruta /movies/{id}
@movie_router.get(
    "/movies/{id}",
    tags=["movies"],
    response_model=Movie,
    status_code=status.HTTP_200_OK,
)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(
            content={"message": "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND
        )

    return JSONResponse(
        content=jsonable_encoder(result), status_code=status.HTTP_200_OK
    )


# Ruta de acceso con parametros query
@movie_router.get(
    "/movies/",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
)
def get_movie_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(
            content={"message": "No encontrado"}, status_code=status.HTTP_404_NOT_FOUND
        )

    return JSONResponse(
        content=jsonable_encoder(result), status_code=status.HTTP_200_OK
    )


# Metodo POST
@movie_router.post(
    "/movies", tags=["movies"], response_model=dict, status_code=status.HTTP_201_CREATED
)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    # movies.append(movie.model_dump())
    return JSONResponse(
        content={"message": "Se ha registrado la pelicula."},
        status_code=status.HTTP_201_CREATED,
    )


# Metodo PUT
@movie_router.put(
    "/movies/{id}", tags=["movies"], response_model=dict, status_code=status.HTTP_200_OK
)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
        return JSONResponse(
            content={"message": "No se ha encontrado la pelicula."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    MovieService(db).update_movie(id, movie)
    return JSONResponse(
        content={"message": "Se ha modificado la pelicula."},
        status_code=status.HTTP_200_OK,
    )


# Metodo DELETE
@movie_router.delete("/movies/{id}", tags=["movies"], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
        return JSONResponse(
            content={"message": "No se ha encontrado la pelicula."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    MovieService(db).delete_movie(id)

    return JSONResponse(
        content={"message": "Se ha eliminado la pelicula."},
        status_code=status.HTTP_200_OK,
    )
