from fastapi import  FastAPI, APIRouter, APIRouter, HTTPException
# from routers import router1 as api_router
# from tasks import router as tasks_router
# from v1.helper import testfunc as omg
from starlette.config import Config
from pinotdb import connect
from pymongo import MongoClient


# conn = connect(host='localhost', port=8000, path='/query/sql', scheme='http')
# curs = conn.cursor()

app = FastAPI()
# api.py

# app.include_router(api_router)
# app.include_router(tasks_router)

# omg.sayhello()

client = MongoClient('mongodb://127.0.0.1:27017')

router = APIRouter()
# 呼び出し
@app.get("/")
async def read_api():

    db = client['example_db']
    collection = db['example_collection']
    
    collection.insert_one({"name": "yuhki", "age": 200})

    collection.insert_many([
        {"name": "Jane1", "age": 25},
        {"name": "Doe2", "age": 35}
    ]) 
    return {"data from pinot":  """ collection.find_one() """} 

@app.get("/test", description="This is the root endpoint", tags=["root"])
async def root():
    db = client['example_db']
    collection = db['example_collection']
    documents = collection.find()
    for document in documents:
        print(document)
        
    return {"result": 'ss'}  # This is the response


@app.get("/example")
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