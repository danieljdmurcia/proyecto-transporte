import json
import os

if not os.path.exists("data"):
    os.makedirs("data")

def guardar_datos(nombre_archivo, datos):
    with open(f"data/{nombre_archivo}.json", "w") as f:
        json.dump(datos, f, indent=4)

def cargar_datos(nombre_archivo):
    ruta = f"data/{nombre_archivo}.json"
    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            return json.load(f)
    return []
