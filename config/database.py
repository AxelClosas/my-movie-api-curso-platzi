import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Creamos una variable con el nombre de la base de datos
sqlite_file_name = "../database.sqlite"

# Lee el directorio actual del archivo database.py
base_dir = os.path.dirname(os.path.realpath(__file__))

# URL Database
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Motor de la base de datos
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
