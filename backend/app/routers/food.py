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
    
# - Search Food
@router.get("/search")
async def search_user(food: SearchFood, token=Depends(auth.wrapper)):
    return await search_foods(food.name, token["sub"])