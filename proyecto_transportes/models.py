from pydantic import BaseModel

class Vehiculo(BaseModel):
    id: int
    placa: str
    marca: str
    modelo: int

class Destino(BaseModel):
    id: int
    ciudad: str
    distancia_km: float
