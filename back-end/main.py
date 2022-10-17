# from flask import Flask
# from flask_restful import Resource, Api
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# api = Api(app)

from typing import List, Union
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI

# importing SQL settings and driver 
from sqlalchemy import create_engine
from databaseConfig import postgres 

from sqlalchemy.orm import sessionmaker



app = FastAPI()

def get_engeine(user:str, password:str, host:str, port:str|int, db:str):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    return create_engine(url)

db = get_engeine(
    postgres["user"],
    postgres["password"],
    postgres["host"],
    postgres["port"],
    postgres["db"]
)


@app.get("/tables")
async def table_names():

    table_names:List[str] = db.table_names()

    return {"tables": table_names}


@app.get("/tables/{table}")
async def get_table(table:str):

    result = db.execute(f"select * from {table}")
    anyList:List[str] =[]

    for i in result:
        anyList.append(i)

    return {table: anyList}



class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()