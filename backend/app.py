import uvicorn
from fastapi import FastAPI
import db  # Import the MongoDB connection
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import APIRouter
app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])



if __name__ == "__app__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)