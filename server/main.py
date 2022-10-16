
import os
from fastapi import FastAPI

# importing SQL settings and driver 
from sqlalchemy import create_engine
from databaseConfig import postgres 

USERTEST = os.getenv('USERTEST', 'test')

app = FastAPI()

db = create_engine(USERTEST)



@app.get("/")
async def root():
    return {"text": "Hello World"}


@app.get("/info")
async def get_info():
    return {
        "url BD": USERTEST,
        
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

    return {table: anyList}

# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", log_level="info")
#     server = uvicorn.Server(config)
#     server.run()