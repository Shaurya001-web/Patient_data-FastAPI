from fastapi import FastAPI, Path , HTTPException ,Query
import json

app=FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data=json.load(f)
        return data

@app.get('/view')
def view():
    data=load_data()

    return data
@app.get('/view/{patient_id}')
def patient_detail(patient_id : str= Path(..., description="A typical patient id looks like", example="P001")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
@app.get("/sort")
def sorted_patients(sort_by:str=Query(...,description="Sort on the basis of height ,bmi and weight "),order :str=Query('asc', description="sort in asc or desc order")):
    valid_sort_list=["height","weight","bmi"]
    if sort_by not in valid_sort_list:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_sort_list}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc or desc')
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data

