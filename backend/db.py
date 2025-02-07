import os
from pymongo import MongoClient
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
MONGO_URI = os.getenv('MONGODB_URI')
if not MONGO_URI:
    raise ValueError("MONGODB_URI is not set in .env")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("auth_db")

async def connect_to_mongo():
    try:
        await client.admin.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        raise

def get_db():
    return db


