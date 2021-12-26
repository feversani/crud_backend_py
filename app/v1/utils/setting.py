#Acá importo las credenciales de la base de datos desde el .env

"""Primero importamos las librerías que necesitaremos, en este caso os para poder leer las variables
de entorno, la clase BaseSettings y la función load_dotenv de la librería python-dotenv la cual 
se encargará de leer las variables de entorno"""

import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Setting(BaseSettings):
    
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_NAME')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

