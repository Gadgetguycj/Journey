from app import database
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from bson.objectid import ObjectId
import motor.motor_asyncio 

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.Journey
foods = db["food"]
def food_helper(food:dict ) -> dict:
    return{
        "id": str(food["_id"]),
        "user_id": str(food["user_id"]),
        "name": str(food["name"]),
        "total_calories": food["total_calories"],
        "total_fat": food["total_fat"],
        "total_carbs":food["total_carbs"],
        "total_protein":food["total_protein"],
    }

async def create_new_food(food: dict):
    food_json = jsonable_encoder(food)
    print(food_json)
    food_json["name"] = food_json["name"].lower()
    await foods.insert_one(food_json)
    raise HTTPException(status_code=201, detail="Added Food")

async def search_foods(food: str, id: str):
    food = food.lower()
    food_exist = await foods.find_one({"name": food, "user_id": id})
    if food_exist:
        return food_helper(food_exist)
    else:
        raise HTTPException(status_code=403, detail="Food Does Not Match Any Existing Entries")