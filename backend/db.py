from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load MongoDB URI from .env file
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Function to check if MongoDB is connected
def is_connected():
    try:
        # Send a ping command to MongoDB to check connection
        client.admin.command('ping')
        return True
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return False
