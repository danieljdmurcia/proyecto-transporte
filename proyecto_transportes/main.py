from fastapi import FastAPI, HTTPException
from models import Vehiculo, Destino
from database import guardar_datos, cargar_datos

app = FastAPI(title="Transportes Sigmotoa")

@app.get("/vehiculos")
def listar_vehiculos():
    return cargar_datos("vehiculos")

@app.post("/vehiculos")
def crear_vehiculo(v: Vehiculo):
    vehiculos = cargar_datos("vehiculos")
    vehiculos.append(v.dict())
    guardar_datos("vehiculos", vehiculos)
    return {"mensaje": "Vehículo agregado"}

@app.put("/vehiculos/{id}")
def actualizar_vehiculo(id: int, v: Vehiculo):
    vehiculos = cargar_datos("vehiculos")
    for i, item in enumerate(vehiculos):
        if item["id"] == id:
            vehiculos[i] = v.dict()
            guardar_datos("vehiculos", vehiculos)
            return {"mensaje": "Vehículo actualizado"}
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")

@app.delete("/vehiculos/{id}")
def borrar_vehiculo(id: int):
    vehiculos = cargar_datos("vehiculos")
    vehiculos = [v for v in vehiculos if v["id"] != id]
    guardar_datos("vehiculos", vehiculos)
    return {"mensaje": "Vehículo eliminado"}

@app.get("/destinos")
def listar_destinos():
    return cargar_datos("destinos")

@app.post("/destinos")
def crear_destino(d: Destino):
    destinos = cargar_datos("destinos")
    destinos.append(d.dict())
    guardar_datos("destinos", destinos)
    return {"mensaje": "Destino agregado"}
