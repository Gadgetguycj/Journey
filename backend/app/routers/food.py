from ..dependencies import *
from app.schemas.food import *
from app.crud.food import *

auth = AuthHandler()
router = APIRouter()

#---API Endpoints---

# - Create Food
@router.post("")
async def create_food(food: CreateNewFood, token=Depends(auth.wrapper)):
    food.user_id = token["sub"]
    return await create_new_food(food)

# - Get Food
@router.get("")
async def get_food(token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
    return await get_foods(token["sub"], skip, limit)

# # - Get Custom Foods
# @router.get("/custom")
# async def get_food(token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
#     return get_foods(str(token["sub"]), skip, limit)
    
# - Search Foods
@router.get("/search")
async def search_user(food: SearchFood, token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
    return await search_foods(str(token["sub"]), food.name, skip, limit)