from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

# uvicorn main:app --reload    For Run

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(...,description="your id")]
    name: Annotated[str, Field(...,description="your name")]
    city: Annotated[str, Field(..., description="your city")]
    age: Annotated[int, Field(...,gt=0, lt= 100, description="your age")]
    gender: Annotated[Literal['male','female', 'others'], Field(..., description="Gender of pat")]
    height: Annotated[float,Field(...,gt = 0, description="your height")]
    weight: Annotated[float, Field(..., gt=0, description="weight of pt")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return  'underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message': 'API to manage your patients records'}

@app.get('/about')
def about():
    return {'message' : 'API to manage patient record'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patients/{patients_id}')
def view_patients(patients_id: str = Path(..., description='ID of the patient in the DB')):
    # .... = req. path,path= add description, min,max length, example   same as Query
    # load all patient
    data = load_data()
    if patients_id in data:
        return data[patients_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invaild field select from {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invaild order')
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse= sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    # load exist data
    data = load_data()
    # check if data already exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient exists')
    # new add to database
    data[patient.id] = patient.model_dump(exclude=['id'])
    # exclude 'id' means remove id from given data
    # save into json file
    save_data(data)
    return JSONResponse(status_code=201, content={'message':'patient created sucessfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    existing_patient_info = data[patient_id]
    update_patient_info = patient_update.model_dump(exclude_unset= True)
    for key, value in update_patient_info.items():
        existing_patient_info[key] = value
    # existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    # pydantic obj -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')
    # add this dict to data
    data[patient_id] = existing_patient_info
    # save data
    save_data(data)
    return JSONResponse(status_code=200, content={'message':'patient updated'})