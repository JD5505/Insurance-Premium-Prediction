from pydantic import BaseModel, computed_field, Field, field_validator
from typing import Annotated, Literal, Optional
from config.city_tier import tier_1_cities, tier_2_cities


# Pydantic model to validate incoming data
class UserInput(BaseModel):
    age : Annotated[int, Field(..., gt=0, lt=120, description="Age of the customer")]
    height : Annotated[float, Field(...,gt=1.0, lt=3.0, description="Height of the client")]
    weight : Annotated[float, Field(...,gt=0, lt=120, description="Weight of the client")]
    income_lpa : Annotated[float, Field(..., description="Income of customer in lpa")]
    smoker : Annotated[bool, Field(..., description="Is a smoker or not")]
    city : Annotated[str, Field(..., description="The city customer lives in")]
    occupation : Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="The occupation of the customer")]
    
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        v = v.strip().title()
        return v
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else: 
            return "senior" 