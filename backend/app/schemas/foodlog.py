from typing import Optional
from pydantic import BaseModel, EmailStr, Field
class CreateNewFoodlog(BaseModel):
    user_id: Optional[str]
    date: str = Field(..., example="07092021")
    name: str=Field(..., example="Hot Dog")
    total_calories: int = Field(..., example="Ammount of Kcals")
    total_fat: int = Field(..., example="Fat content in grams")
    total_carbs: int = Field(..., example="Carbohydrate content in grams")
    total_protein: int = Field(..., example="Total protein content in grams")

class SearchFood(BaseModel):
    name: str = Field(..., example= "hot dog")