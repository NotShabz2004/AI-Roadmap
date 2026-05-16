from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print("inserted")


def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")


patient_info = {
    "name": "Shahbaz",
    "email": "shaz@gmail.com",
    "linkedin_url": "https://claude.ai",
    "age": 22,
    "weight": 80.1,
    "married": False,
    "contact_details": {"phone": "29384723"},
}

Patient1 = Patient(**patient_info)

insert_patient(Patient1)
