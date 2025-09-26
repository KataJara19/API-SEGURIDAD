**API LOGIN**

1. IMPLEMENTACIONES

- Uso de **FastAPI** (con el servidor **Uvicorn**)
- Implementación de la librería **SQLModel** para simulación de bdd


2. CONFIGURACIONES

- Prepare su entorno, asegurándose de tener un entorno virtual activo.
- Installe las librerías que se encuentran en requirements.txt

3. EJECUTAR

- emplee el comando: fastapi dev main.py
- Desde su navegador, la API es accesible en la dirección base: http://127.0.0.1:8000/docs.


------------------------------------------------------------------------------------------------

**EJEMPLO**

LOGIN EXITOSO:
-- CREDENDCIALES
{
  "nombre_usuario": "kata",
  "contrasena": "345"
}

--- RESPUESTA:

<img width="835" height="464" alt="image" src="https://github.com/user-attachments/assets/5fe3d038-b4ef-4796-a066-8976ae6ea2d4" />



LOGIN NO EXITOSO:

-- CREDENDCIALES

{
  "nombre_usuario": "JAVIER",
  "contrasena": "345"
}

--- RESPUESTA:
<img width="859" height="438" alt="image" src="https://github.com/user-attachments/assets/fb84c6b0-5225-4d6e-be23-04b74c63e29b" />




