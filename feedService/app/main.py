from fastapi import  FastAPI, APIRouter, APIRouter, HTTPException
from routers import router1 as api_router
# from tasks import router as tasks_router
# from v1.helper import testfunc as omg
from starlette.config import Config
from pinotdb import connect

config = Config(".env")
# POSTGRES_DB = config("POSTGRES_DB", cast=str)
# print(POSTGRES_DB)

#print("Hello World")
print("Hello, world!")
conn = connect(host='localhost', port=8000, path='/query/sql', scheme='http')
curs = conn.cursor()

app = FastAPI()
# api.py

app.include_router(api_router)
# app.include_router(tasks_router)

# omg.sayhello()


router = APIRouter()
# 呼び出し
@app.get("/")
async def read_api():
    ## return {"message": "Hello from API!"}
    curs.execute("""
    SELECT * 
    FROM baseballStats
    WHERE league IN (%(leagues)s)
    """, {"leagues": ["AA", "NL"]})
    for row in curs:
        print(row)
    return {"data from pinot":  row} 

@app.get("/test", description="This is the root endpoint", tags=["root"])
async def root():
    return {"message": "Hello World"}  # This is the response


@app.get("/test/v1/{id}")
async def get(id: int):
    if id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": id}  # This is the response


@app.post("/hello",  tags=["group1"])
async def post():
    return {"message": "Hello World"}  # This is the response


@app.delete("/test/hello")
async def list_items():
    return {"message": "Hello World"}  # This is the response


@app.put("/hello")
async def put():
    return {"message": "Hello World"}  # This is the response