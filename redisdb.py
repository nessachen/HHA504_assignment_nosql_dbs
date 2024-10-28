import redis
import pandas as pd
import json
import os 
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('nosql_hw.csv')

redisDB_password = os.getenv('redisdb_password')

r = redis.StrictRedis(
  host='redis-15010.c228.us-central1-1.gce.redns.redis-cloud.com',
  port=15010,
  password=redisDB_password,
  decode_responses=True)

for _, row in df.iterrows():
    patient_data = row.to_dict()
    r.set(patient_data['PatientID'], json.dumps(patient_data))

print("Patient data stored in Redis successfully.")

