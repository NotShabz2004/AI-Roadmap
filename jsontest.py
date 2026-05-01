from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


@app.get("/view")
def view():
    data = load_data()

    return data


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    # time to load pateints data
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    else:
        return "patient not found"
