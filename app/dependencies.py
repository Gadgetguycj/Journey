from typing import List
import motor.motor_asyncio 
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from app.auth import AuthHandler

#HTTP ERRORS
def http_404():
    raise HTTPException(status_code=404, detail="Resource not found or has been deleted")

def http_403():
    raise HTTPException(status_code=403, detail="Insufficent Authorization")

def http_401():
    raise HTTPException(status_code=401, detail="Not authenticated")

def http_401():
    raise HTTPException(status_code=400, detail="Bad Request")