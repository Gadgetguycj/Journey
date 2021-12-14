from app import database
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from bson.objectid import ObjectId
import motor.motor_asyncio 
import json, re

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.Journey
foodlogs = db["foodlog"]
def foodlog_helper(foodlog:dict ) -> dict:
    return{
        "id": str(foodlog["_id"]),
        "user_id": str(foodlog["user_id"]),
        "date": str(foodlog["name"]),
        "name": str(foodlog["name"]),
        "total_calories": foodlog["total_calories"],
        "total_fat": foodlog["total_fat"],
        "total_carbs":foodlog["total_carbs"],
        "total_protein":foodlog["total_protein"],
    }

async def create_new_foodlog(food: dict):
    food_json = jsonable_encoder(food)
    food_json["name"] = food_json["name"].lower()
    await foodlogs.insert_one(food_json)
    raise HTTPException(status_code=201, detail="Added Food to foodlog")

async def get_foodlog(user_id, date, skip, limit):
    final_foods = []
    food_exist = foodlogs.find( {"$and": [{"$or" : [ {"user_id" : user_id},{"user_id" : "public"}]},{ "date":date}]}).skip(skip).limit(limit)
    if food_exist:
        for food in await food_exist.to_list(length=limit):
            final_foods.append(foodlog_helper(food))
        return final_foods
    else:
        raise HTTPException(status_code=403, detail="Food Does Not Match Any Existing Entries")

async def get_foodlog_calories(user_id, date, skip, limit):
    calories = 0
    food_exist = foodlogs.find( {"$and": [{"$or" : [ {"user_id" : user_id},{"user_id" : "public"}]},{ "date":date}]}).skip(skip).limit(limit)
    if food_exist:
        for food in await food_exist.to_list(length=limit):
            calories+=food["total_calories"]
        return calories
    else:
        raise HTTPException(status_code=403, detail="Food Does Not Match Any Existing Entries")

        
        