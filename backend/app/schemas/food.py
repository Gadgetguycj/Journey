from typing import Optional
from datetime import datetime
from pydantic import *
class CreateNewFood(BaseModel):
    user_id: Optional[int]
    name: str=Field(..., example="Hot Dog")
    total_calories: int = Field(..., example="Ammount of Kcals")
    total_fat: int = Field(..., example="Fat content in grams")
    total_carbs: int = Field(..., example="Carbohydrate content in grams")
    total_protein: int = Field(..., example="Total protein content in grams")

class SearchFood(BaseModel):
    name: str = Field(..., example= "hot dog")