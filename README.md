 Transportes Sigmotoa

Este proyecto es una práctica de desarrollo con FastAPI.
El objetivo es construir un pequeño sistema para administrar los vehículos y destinos de una empresa de transporte llamada Transportes Sigmotoa.

 Descripción

El sistema permite registrar, listar, actualizar y eliminar:

Vehículos (placa, marca, modelo)

Destinos (ciudad y distancia)

La información se guarda en archivos JSON, lo que hace el proyecto sencillo y sin necesidad de bases de datos externas.
 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.9 o superior

FastAPI

Uvicorn



Ejecuta el servidor con:

uvicorn main:app --reload

Estructura del proyecto

proyecto_transportes/
│
├── main.py          
├── models.py       
├── database.py      
├── README.md        
└── data/
    ├── vehiculos.json
    └── destinos.json

Mapa de endpoints
   Vehículos
Método	Endpoint	Descripción	Parámetros	Ejemplo de uso
GET	/vehiculos	Muestra la lista de todos los vehículos registrados.	Ninguno	GET /vehiculos
POST	/vehiculos	Agrega un nuevo vehículo al sistema.	JSON con los campos:
id, placa, marca, modelo	POST /vehiculos → { "id": 1, "placa": "ABC123", "marca": "Chevrolet", "modelo": 2020 }
PUT	/vehiculos/{id}	Actualiza los datos de un vehículo según su ID.	id en la URL + JSON con los nuevos valores	PUT /vehiculos/1
DELETE	/vehiculos/{id}	Elimina un vehículo existente por su ID.	id en la URL	DELETE /vehiculos/1
 Destinos
Método	Endpoint	Descripción	Parámetros	Ejemplo de uso
GET	/destinos	Lista todos los destinos disponibles.	Ninguno	GET /destinos
POST	/destinos	Crea un nuevo destino.	JSON con los campos:
id, ciudad, distancia_km	POST /destinos → { "id": 1, "ciudad": "Medellín", "distancia_km": 420 }


Abre el navegador en:

 http://127.0.0.1:8000/docs

Jaider Daniel Murcia Murcia
