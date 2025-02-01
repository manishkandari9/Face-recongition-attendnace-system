import uvicorn
from fastapi import FastAPI
import db  # Import the MongoDB connection
from routes import user_routes 

app = FastAPI()

app.include_router(user_routes.router, prefix="/api/auth")



if __name__ == "__app__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)