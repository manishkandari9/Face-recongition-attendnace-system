import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGODB_URI')
if not MONGO_URI:
    raise ValueError("MONGODB_URI is not set in .env")

client = MongoClient(MONGO_URI)
#  hello word
try:
    client.admin.command('ping')
    print("MongoDB connected successfully!")
except Exception as e:
    print(f"MongoDB connection failed: {e}")



