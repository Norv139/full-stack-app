import os
from typing import List
import uvicorn

# importing fastAPI moduls
from fastapi import FastAPI
from pydantic import BaseModel

# importing SQL settings and driver 
from sqlalchemy import create_engine
from databaseConfig import postgres 

USERTEST = os.getenv('USERTEST', 'postgresql://postgres:postgres@localhost:5432/shop')
db = create_engine(USERTEST)

app = FastAPI()


class IRoot(BaseModel):
    read_doc: str

@app.get("/", response_model=IRoot)
async def root():
    return {
        "read_doc": "/redoc"
    }


class ITables(BaseModel):
    tables: list[str]

@app.get("/tables", response_model=ITables)
async def table_names():

    table_names:list[str] = db.table_names()

    return {"tables": table_names}


class ITable(BaseModel):
    table: list[object]

@app.get("/tables/{table}", response_model=ITable)
async def get_table(table:str) -> list[str]:

    result = db.execute(f"select * from {table}")

    anyList:list[str] = []

    for i in result:
        anyList.append(i)

    return {"table": anyList}


# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", log_level="info")
#     server = uvicorn.Server(config)
#     server.run()