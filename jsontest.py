from fastapi import FastAPI, Path, HTTPException, Query
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
def view_patient(
    patient_id: str = Path(
        ..., description="This is the patient details in DB", example="P001"
    )
):
    # time to load pateints data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sortpatients")
def sortedpatients(
    sort_by: str = Query(
        ..., description="Sorted list of patients on basis of height, weight, bmi"
    ),
    order: str = Query("asc", description="Sort in ascending here"),
):
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Pls choose from  {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Please choose asc or desc.")
    data = load_data()
    check = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=check)
    return sorted_data
