from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}       
# dynamic path parameter 


@app.get("/about/{name}")
def about(name:str):
    return {"About":  "This is a simple FastAPI application.",
            "name": name}

# QUERY PARAMETER (?name=value)


@app.get("/contactus")
def contact_us(name:str=None ,price:int=0):
    return {"Contact": "Found your in query parameter",
            "name": name,
            "price": price}

# POST REQUEST

@app.post("/create")
def create_item(name:str, price:float):
    return {"message": "Item created successfully",
            "name": name,
            "price": price}

# Pydantic model for request body
from pydantic import BaseModel
class User(BaseModel):
    name: str
    email: str  
    age: int    

@app.post("/create_user")
def create_user(user:User):
    return {"message": "User created successfully",
            "user": user}