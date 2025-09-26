from fastapi import FastAPI
from sqlmodel import SQLModel


class Usuario(SQLModel):
    nombre_usuario: str
    contrasena: str
    
    
BDD = [
    Usuario(nombre_usuario="admin", contrasena="123"), Usuario(nombre_usuario="kata", contrasena="345") ]

class Credenciales (SQLModel):
    nombre_usuario: str
    contrasena: str
    

app = FastAPI()


@app.post("/login")

def verificarLogin(datos: Credenciales):
    
    for usuario in BDD:
        
        if usuario.nombre_usuario == datos.nombre_usuario and usuario.contrasena == datos.contrasena:
            
            return {"mensaje": "Login exitoso"}
        
    return {"mensaje": "Login no exitoso"}
    
