
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from Model.predict import user_input, MODEL_VERSION, model
from schema.user_output import UserOutput
from schema.user_input import UserInput

app = FastAPI()

@app.get('/')
def home():
    return {'Message' : 'Insurance Premium Prediction API'}
        
@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version': MODEL_VERSION,
        'Port': 'http://127.0.0.1:8000',
        'model loaded' : model is not None
    }

@app.post("/predict", response_model = UserOutput)
def predict_premium(data : UserInput):
    input_df = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    try:
        prediction = user_input(input_df)
        return JSONResponse(status_code=200, content={'Predicted_category': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e)) 