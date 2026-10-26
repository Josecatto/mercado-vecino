import os
from pathlib import Path


def leer_secreto(nombre: str) -> str:
    ruta = os.getenv(f"{nombre}_FILE")
    if ruta and Path(ruta).exists():
        return Path(ruta).read_text().strip()
    valor = os.getenv(nombre)
    if valor is None:
        raise RuntimeError(f"Falta la configuración {nombre}")
    return valor


DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mercado")
DB_USER = os.getenv("DB_USER", "mercado_app")
DB_PASSWORD = leer_secreto("DB_PASSWORD")
