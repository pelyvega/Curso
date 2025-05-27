from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
# Creación de modelo
class Products(BaseModel):
    id: int
    name: str
    price: float

class Users(BaseModel):
    id: int
    name: str
    email: str

class Orders(BaseModel):
    id: int
    user_id: int
    product_id: List[int]



# Base de datos en memoria
products  = []
users     = []
orders    = []

@app.post("/products") #Ruta
def create_product(prod: Products): #Endpint
    products.append(prod)
    return "Guardado con éxito"

@app.get("/products",response_model=List[Products]) #Ruta
def list_prodects():
    return products