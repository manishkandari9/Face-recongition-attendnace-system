from fastapi import FastAPI
import db  # Import the MongoDB connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MongoDB connection successful!"}
