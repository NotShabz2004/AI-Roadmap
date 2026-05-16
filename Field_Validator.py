from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        # we have to extract whats after @
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("wrong age")


def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")


patient_info = {
    "name": "Shahbaz",
    "email": "shaz@hdfc.com",
    "linkedin_url": "https://claude.ai",
    "age": 22,
    "weight": 80.1,
    "allergies": ["pollen", "dust"],
    "married": False,
    "contact_details": {"phone": "29384723"},
}

Patient1 = Patient(**patient_info)

insert_patient(Patient1)
