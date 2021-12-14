from app import database
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, HTTPException, APIRouter, Body
from bson.objectid import ObjectId
import motor.motor_asyncio 
from passlib.context import CryptContext
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd.hash(password)
def check_password_hash(password, password_hashed):
    return True if pwd.verify(password, password_hashed) else False


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.Journey



# users_collection = database.db.get_collection("users")
# recipes_collection = database.db.get_collection("recipes")
# diet_plans_collection = database.db.get_collection("diet_plans")
# workout_plan_collection = database.db.get_collection("workout_plans")
# health_log_collection = database.db.get_collection("health_logs")
# foods_collection = database.db.get_collection("foods")

# ---Helper Methods---
def user_public_data_helper(user) -> dict:
    return{
        "id": str(user["_id"]),
        "fullname": user["fullname"],
    }

def user_private_data_helper(user) -> dict:
    return{
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "weight": user["weight"],
        "height": user["height"],
        "age": user["age"],
    }

def filter_empty_dict(input:dict):
    filtered_dict = {}
    for key in input:
        if input[key]!=None:
            filtered_dict[key]=input[key]
    return filtered_dict

#----Create----
async def create_new_user(user_data: dict) -> dict:
    
    user_data = jsonable_encoder(user_data)
    check_for_email = await db["users"].find_one({"email": user_data["email"]})

    #If email exists, return error
    if check_for_email:
        raise HTTPException(status_code=401, detail="email already in use")
    
    #If email doesn't exist, create user
    else:
        user_data["user_type"] = 1
        user_data["password"] = get_password_hash(user_data["password"])
        user = await db["users"].insert_one(user_data)
        new_user = jsonable_encoder(await db["users"].find_one({"id": user.inserted_id}))
        print(new_user)
        raise HTTPException(status_code=201, detail="User Created")
        

#----Retrieve----
async def retrieve_private_user_data(id: str):
    user = await db["users"].find_one({"_id": ObjectId(id)})
    if user:
        return user_private_data_helper(user)

async def check_password(email, password):
    user_lookup = await db["users"].find_one({"email": email})

    if user_lookup:
        user_password_hash = user_lookup["password"]
        verify = check_password_hash(password, user_password_hash)

        if verify:
            return user_lookup
        else:
            raise HTTPException(status_code=401, detail = "Invalid email and/or passowrd")
    else:
        raise HTTPException(status_code=401, detail = "Invalid email and/or passowrd")


# ----Update----
async def update_user_data(user_data: dict, id: str):
    user_data = filter_empty_dict(user_data)
    user_data = jsonable_encoder(user_data)
    print(id)
    print(user_data)

    user_update = await db["users"].update_one({"_id": ObjectId(id)}, {'$set': user_data})
    if user_update:
        raise HTTPException(status_code=202, detail="User Updated")


#----Delete----
# async def delete_user(id:str):
#     delete_user_health_data = await db["health_log"].delete_many({"_id": ObjectId(id)})
#     delete_user = await db["users"].delete_one({"_id": ObjectId(id)})

#     raise HTTPException(status_code=204, detail="User Account Deleted")


# #----Create----
# async def create_new_user(user_data: dict) -> dict:
#     user = await users_collection.insert_one(user_data)
#     new_user = await users_collection.find_one({"_id": user.inserted_id})
#     return user_public_data_helper(new_user)