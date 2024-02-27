from fastapi import  FastAPI, APIRouter, APIRouter, HTTPException
# from routers import router1 as api_router
# from tasks import router as tasks_router
# from v1.helper import testfunc as omg
from starlette.config import Config
from pinotdb import connect
from pymongo import MongoClient
from pydantic import BaseModel
from kafka import KafkaConsumer
from kafka import TopicPartition
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

# conn = connect(host='localhost', port=8000, path='/query/sql', scheme='http')
# curs = conn.cursor()
class Item(BaseModel):  
    name: str
    age: int

app = FastAPI()
# api.py



# app.include_router(api_router)
# app.include_router(tasks_router)

# omg.sayhello()





@app.get("/")
async def read_api():
    print("Hello, world!")
    producer = KafkaProducer(bootstrap_servers='localhost:29092')
    topic_name = 'test-topic'

    # メッセージを送信
    producer.send(topic_name, b'Hello, This is a message from producer!')
    producer.send(topic_name, b'Hello, This is a second message from producer123!')
    producer.flush()  # すべての非同期メッセージが送信されるまで待機

    print('Message sent to topic:', topic_name)




    return {"data from kafka":  'producer'} 

@app.get("/test", description="This is the root endpoint日本語", tags=["root"])
async def root():
    db = client['example_db']
    collection = db['example_collection']
    documents = collection.find()
    for document in documents:
        print(document)
        
    return {"result": 'ss'}  # This is the response


@app.get("/example/{id}")
async def get(id: int):
    if id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": id}  # This is the response


@app.post("/hello",  tags=["group1"])
async def post(item: Item):
    
    db = client['example_db']
    collection = db['example_collection']
    collection.insert_one({"name": item.name, "age": item.age})
    
    return {"message": 'aaa'}  # This is the response


@app.delete("/test/hello")
async def list_items():
    return {"message": "Hello World"}  # This is the response


@app.put("/hello")
async def put():
    return {"message": "Hello World"}  # This is the response