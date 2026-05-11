from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give name of patient in less than 50 characters",
            examples=["Shahbaz", "Malik"],
        ),
    ]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: Annotated[bool, Field(default=None, description="Married or Single")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
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
