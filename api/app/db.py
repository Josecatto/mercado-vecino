import psycopg

from app.config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def obtener_conexion():
    return psycopg.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
