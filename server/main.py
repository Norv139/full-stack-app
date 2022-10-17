
import json
import os
import uvicorn

# importing fastAPI moduls
from fastapi import FastAPI, Response

# importing SQL settings and driver 
from sqlalchemy import create_engine
from databaseConfig import postgres 

USERTEST = os.getenv('USERTEST', 'postgresql://postgres:postgres@localhost:5432/shop')


description = """
    ChimichangApp API helps you do awesome stuff. 🚀

    ## Items

    You can **read items**.

    ## Users

    You will be able to:

    * **Create users** (_not implemented_).
    * **Read users** (_not implemented_).
"""

app = FastAPI()




db = create_engine(USERTEST)

@app.get("/")
async def root():
    return {
        "read doc": "/redoc"
    }

@app.get("/tables")
async def table_names():

    table_names = db.table_names()

    return {"tables": table_names}

@app.get("/tables/{table}")
async def get_table(table:str):

    result = db.execute(f"select * from {table}")

    anyList = []

    for i in result:
        anyList.append(i)

    return Response(content={table: anyList}, media_type="application/json")

# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", log_level="info")
#     server = uvicorn.Server(config)
#     server.run()