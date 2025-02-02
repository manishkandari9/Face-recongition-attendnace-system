import uvicorn
from fastapi import FastAPI
import db  # Import the MongoDB connection
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, attendance, users, websocket
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

# Include routes
app.include_router(auth.router)
app.include_router(attendance.router)
app.include_router(users.router)
app.include_router(websocket.router)



if __name__ == "__app__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)