from fastapi import FastAPI

from app.db import obtener_conexion

app = FastAPI(title="Mercado Vecino API")


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.get("/tiendas")
def listar_tiendas():
    with obtener_conexion() as conn:
        filas = conn.execute("SELECT id, nombre, barrio FROM tiendas").fetchall()
    return [{"id": f[0], "nombre": f[1], "barrio": f[2]} for f in filas]
