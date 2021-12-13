import motor.motor_asyncio 
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.Journey

#----Helper Functions----
#retrieve only public facing data
def user_public_data_helper(user) -> dict:
    return{
        "id": str(user("_id")),
        "fullname": user["fullname"],
        "active_workout_plan": user["active_workout_plan"],
        "active_diet_plan": user["active_diet_plan"],
    }

def user_private_data_helper(user) -> dict:
    return{
        "email": EmailStr["email"],

    }
