# Bring in lightweight dependencies
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

# class ScoringItem(BaseModel): 
#     YearsAtCompany: float #/ 1, // Float value 
#     EmployeeSatisfaction: float #0.01, // Float value 
#     Position:str # "Non-Manager", # Manager or Non-Manager
#     Salary: int #4.0 // Ordinal 1,2,3,4,5

# with open('rfmodel.pkl', 'rb') as f: 
#     model = pickle.load(f)

# @app.post('/')
# async def scoring_endpoint(item:ScoringItem): 
#     df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
#     yhat = model.predict(df)
#     return {"prediction":int(yhat)}

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(data: BankNote):
    print(data)
    data = data.dict()
    print(data)
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = rfmodel.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Its a Bank note"
    return {"prediction": prediction}
    