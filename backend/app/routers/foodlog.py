from ..dependencies import *
from app.schemas.foodlog import *
from app.crud.foodlog import *

auth = AuthHandler()
router = APIRouter()

#---API Endpoints---

# - Add food to foodlog
@router.post("")
async def create_foodlog(foodlog: CreateNewFoodlog, token=Depends(auth.wrapper)):
    foodlog.user_id = token["sub"]
    return await create_new_foodlog(foodlog)

# - Get Foodlog
@router.get("/{date}")
async def get_food(date, token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
    return await get_foodlog(token["sub"], date, skip, limit)

# - Get Foodlog calories
@router.get("/{date}/calories")
async def get_food(date, token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
    return await get_foodlog_calories(token["sub"], date, skip, limit)

# # - Get Custom Foods
# @router.get("/custom")
# async def get_food(token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
#     return get_foods(str(token["sub"]), skip, limit)
    
# - Search Foods
@router.get("/search")
async def search_user(food: SearchFood, token=Depends(auth.wrapper), skip: int = 0, limit: int = 100):
    return await search_foods(str(token["sub"]), food.name, skip, limit)