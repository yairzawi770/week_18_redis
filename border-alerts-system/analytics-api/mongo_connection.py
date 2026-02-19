import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
mongo_client = MongoClient(MONGO_URI)
orders_col = mongo_client["border_alerts"]["alerts"]
