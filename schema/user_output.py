from pydantic import BaseModel, Field
from typing import Annotated

class UserOutput(BaseModel):
    prediction : Annotated[str, Field(..., description = "The Insurance premium according to your conditions", example="High")]

