from fastapi import FastAPI,Request
from pydantic import BaseModel

app=FastAPI()


class Helloj(BaseModel):
    name:str="abc"
    format:str="json"


@app.post("/helloj")
def helloj(hello:Helloj): 
    return dict(name=hello.name,format=hello.format)
    
@app.get("/helloj/{name}/{format}")
@app.get("/helloj")
def helloj(name:str='abc',format:str='json'):
    return dict(name=name,format=format)
    
