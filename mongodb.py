import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os 
from dotenv import load_dotenv

load_dotenv()

mongoDB_password = os.getenv('mongodb_password')

uri = f'mongodb+srv://nessa-test:{mongoDB_password}@nessa-test.r1qip.mongodb.net/?retryWrites=true&w=majority&appName=nessa-test'
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

df = pd.read_csv('nosql_hw.csv')

data = df.to_dict(orient='records')

db = client['hha504-nosql-hw']
collection = db['healthcare-data']

collection.insert_many(data)

print("data inserted")