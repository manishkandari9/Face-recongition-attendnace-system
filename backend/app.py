import uvicorn
from fastapi import FastAPI
import db  # Import the MongoDB connection
from fastapi.middleware.cors import CORSMiddlewareapp = FastAPI()





if __name__ == "__app__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)