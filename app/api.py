#Imports
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, APIRouter, Body
from .auth import AuthHandler
from fastapi.encoders import jsonable_encoder

#Initalize FastAPI
app = FastAPI()

#Root for testing webserver
@app.get("/", tags=["root"])
def check_status():
    raise HTTPException(status_code=200, detail="Okay")

#Route Imports
from app.routers.user import router as UserRouter
from app.routers.food import router as FoodRouter

#Routes
app.include_router(UserRouter, tags=["user"], prefix="/user")
app.include_router(FoodRouter, tags=["food"], prefix="/food")



#CORS
origins = [
    "http://journey.gadget.sh",
    "http://localhost:3000/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

