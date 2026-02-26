import pandas as pd
import joblib

with open("Model/model.pkl", "rb") as f:
    model = joblib.load(f)

MODEL_VERSION = '1.0.0'

def user_input(input_dict : dict):
    input_df = pd.DataFrame([input_dict])

    output = model.predict(input_df)[0]

    return output