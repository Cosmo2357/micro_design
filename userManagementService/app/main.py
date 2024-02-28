from fastapi import  FastAPI, APIRouter, APIRouter, HTTPException
from starlette.config import Config
from pydantic import BaseModel
from kafka import KafkaConsumer
from kafka import TopicPartition
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import psycopg2
from sqlalchemy import Table, Column, MetaData, Integer, Computed, create_engine, text, String

engine = create_engine('postgresql://my_user:my_password@localhost:5432/postgres')

connection = psycopg2.connect(
                            host='localhost',
                            user='my_user',
                            password='my_password',
                            database='my_database')

class Item(BaseModel):  
    display_name: str
    bio: int
    metadata: json

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    display_name = Column(String, index=True)
    bio = Column(String, index=True)
    
app = FastAPI()


@app.get("/user", description="すべてのユーザーデータを取得します", tags=["root"])
async def getAllUsers():

    return {"result": 'ss'}  # This is the response


@app.get("/user/{id}", description="特定のユーザーデータを取得します")
async def getOneUser(id: int):
    if id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": id}  # This is the response

@app.post("/user", description="ユーザーデータを作ります", tags=["group1"])
async def createUser(item: Item):
    
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