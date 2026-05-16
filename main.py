from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    model_validator,
    field_validator,
    computed_field,
)
from fastapi import FastAPI, HTTPException, Path, Query
from typing import Annotated
import json


class Patient(BaseModel):
    name: Annotated[str, Path(..., description="Name of the Patient")]
    age: Annotated[int, Path(..., description=" Age of the Patient", gt=0, lt=120)]
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height**2)
        return bmi
