import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from .env
MONGO_URI = os.getenv('MONGODB_URI')

# MongoDB connection
client = MongoClient(MONGO_URI)

# Function to check MongoDB connection
def check_mongo_connection():
    try:
        # Attempt to send a ping to MongoDB server to check the connection
        client.admin.command('ping')
        print("MongoDB connected successfully!")  # This will print in the terminal
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

# Call the check function when db.py is imported
check_mongo_connection()
