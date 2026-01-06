from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()


class Patients(BaseModel):
    id: Annotated[str, Field(..., description="Patient ID", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient", examples=["John"])]
    city: Annotated[str, Field(..., description="City of the patient", examples=["Pune"])]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the patient", examples=["male"])
    ]
    age: Annotated[int, Field(..., gt=0, le=18, description="Age of the patient", examples=[17])]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient", examples=[1.85])]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient", examples=[70])]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        else:
            return "Obese"


class Patients_update(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    gender: Annotated[Optional[Literal["male", "female", "others"]], Field(default=None)]
    age: Annotated[Optional[int], Field(gt=0, le=18, default=None)]
    height: Annotated[Optional[float], Field(gt=0, default=None)]
    weight: Annotated[Optional[float], Field(gt=0, default=None)]


def load_data():
    with open("patient.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("patient.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/view")
def view():
    return load_data()


@app.get("/view/{patient_id}")
def patient_detail(
    patient_id: str = Path(..., description="A typical patient id looks like", example="P001")
):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sorted_patients(
    sort_by: str = Query(..., description="Sort on the basis of height ,bmi and weight"),
    order: str = Query("asc", description="sort in asc or desc order")
):
    valid_sort_list = ["height", "weight", "bmi"]
    if sort_by not in valid_sort_list:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_sort_list}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order select between asc or desc")

    data = load_data()
    sort_order = True if order == "desc" else False

    patients = [Patients(id=k, **v) for k, v in data.items()]
    sorted_data = sorted(
        patients,
        key=lambda p: getattr(p, sort_by),
        reverse=sort_order
    )

    return [p.model_dump() for p in sorted_data]


@app.post("/create")
def create_patient(patients: Patients):
    data = load_data()
    if patients.id in data:
        raise HTTPException(status_code=400, detail="The patient data exist in the data base")

    data[patients.id] = patients.model_dump(exclude=["id"])
    save_data(data)

    return JSONResponse(
        status_code=201,
        content="The patient details has been added to data base"
    )


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: Patients_update):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient_data = data[patient_id]
    update_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in update_patient_info.items():
        existing_patient_data[key] = value

    data[patient_id] = existing_patient_data
    save_data(data)

    return {"message": "Patient updated successfully"}
