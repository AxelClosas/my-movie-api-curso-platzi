from pydantic import BaseModel, Field
from typing import Optional, List


# Creamos la clase Movie
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=3, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(gt=0.0, le=10.0)
    category: str = Field(min_length=5, max_length=10)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi Pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2024,
                "rating": 10.0,
                "category": "Acción",
            }
        }
