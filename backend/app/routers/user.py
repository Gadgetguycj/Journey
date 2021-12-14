from ..dependencies import *
from app.schemas.user import *
from app.crud.user import *

auth = AuthHandler()
router = APIRouter()


#Compares the user's token to what they're requesting
def check_auth(token, user):
    if token["sub"] == user.id: return True #If user wants to edit their own resource
    elif token["tid"] >= 2: return True #If Admin wants to edit their resource
    else: return False #Neither is True, auth check fails


#---API Endpoints---


# - Create User
@router.post("")
async def create_user(user: CreateUserSchema):
    return await create_new_user(user.dict())

# - Authenticate user and return JWT on successful login
@router.post("/login")
async def login_user(user: LoginUserSchema):
    result = await check_password(user.email, user.password)
    if result != None:
        token = auth.encode_token(str(result["_id"]), str(result["user_type"]))
        return {"token": token}

# - Get User
@router.get("")
async def get_user(token=Depends(auth.wrapper)):
    return await retrieve_private_user_data(token["sub"])

# - Get User Calories
@router.get("/calories")
async def get_user(token=Depends(auth.wrapper)):
    info = await retrieve_private_user_data(token["sub"])
    calories = 10.0462 * info["weight"] + 5.46063 * info["height"] - 5 * info["age"] + 5
    return  calories

# - Edit User
@router.patch("")
async def update_user(user: SearchUserSchema, token=Depends(auth.wrapper)):
    return await update_user_data(user.dict(), str(token["sub"]))

# - Get Specific User
@router.get("/{user_id}")
async def get_id_user(user_id, token=Depends(auth.wrapper)):
    if token["sub"] == user_id:
        return await retrieve_private_user_data(token["sub"])
    raise HTTPException(status_code=409, detail="User already exists")





























    

# - Delete Users
# @router.delete("/{user_id}")
# async def delete_user(user_id: int, token=Depends(auth.wrapper)):
#     #if crud operation successful:
#     raise HTTPException(status_code=200, detail="User has been successfully deleted")
#     #if crud operation not successful:
#     raise HTTPException(status_code=400, detail="Request Failed")

