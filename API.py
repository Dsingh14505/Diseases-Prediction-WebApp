from fastapi import FastAPI
from pydantic import BaseModel
import requests
import pickle 
import numpy as np 
import pandas as pd
import os

app = FastAPI()

# Load Saved Models 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

heart_model_path = os.path.join(BASE_DIR, "saved_models", "heart.sav")
heart_model = pickle.load(open(heart_model_path, "rb"))

diabetes_model_path = os.path.join(BASE_DIR, "saved_models", "diabetes.sav")
diabetes_model = pickle.load(open(diabetes_model_path, "rb"))

breast_cancer_model_path = os.path.join(BASE_DIR, "saved_models", "breast_cancer.sav")
breast_cancer_model = pickle.load(open(breast_cancer_model_path, "rb"))

class heart_inputs(BaseModel):
        age : float
        sex : float
        cp : float
        trestbps : float
        chol : float
        fbs : float
        restecg : float
        thalach : float
        exang : float
        oldpeak : float
        slope : float
        ca : float
        thal : float

class diabetes_inputs(BaseModel):
        Pregnancies : float
        Glucose : float
        BloodPressure : float
        SkinThickness : float
        Insulin : float
        BMI : float
        DiabetesPedigreeFunction : float
        Age : float

class breast_cancer_inputs(BaseModel):
    radius_mean : float
    texture_mean : float
    perimeter_mean : float
    area_mean : float
    smoothness_mean : float
    compactness_mean : float
    concavity_mean : float
    concave_points_mean : float
    symmetry_mean : float
    fractal_dimension_mean : float
    radius_se : float
    texture_se : float
    perimeter_se : float
    area_se : float
    smoothness_se : float
    compactness_se : float
    concavity_se : float
    concave_points_se : float
    symmetry_se : float
    fractal_dimension_se : float
    radius_worst : float
    texture_worst : float
    perimeter_worst : float
    area_worst : float
    smoothness_worst : float
    compactness_worst : float
    concavity_worst : float
    concave_points_worst : float
    symmetry_worst : float
    fractal_dimension_worst : float

@app.get("/")
def home():
    return {"message":" Disease api is running"}

@app.post("/predict/heart")
def heart_predict(input_data : heart_inputs):
    inputs_for_prd = np.array([[
        input_data.age,
        input_data.sex,
        input_data.cp,
        input_data.trestbps,
        input_data.chol,
        input_data.fbs,
        input_data.restecg,
        input_data.thalach,
        input_data.exang,
        input_data.oldpeak,
        input_data.slope,
        input_data.ca,
        input_data.thal
    ]])
    df_heart = pd.DataFrame(inputs_for_prd, columns= heart_model['features_name'])
    for_heart_prd = heart_model['model'].predict(df_heart)

    if for_heart_prd[0] == 1:
        return {"prediction" :"Heart Disease Detected"}
    else:
        return {"prediction" :"Healthy Heart"}

@app.post("/predict/diabetes")
def diabetes_predict(input_data : diabetes_inputs):
    inputs_for_prd = np.array([[
        input_data.Pregnancies,
        input_data.Glucose,
        input_data.BloodPressure, 
        input_data.SkinThickness, 
        input_data.Insulin,
        input_data.BMI, 
        input_data.DiabetesPedigreeFunction,
        input_data.Age
                            ]])

    df_diabetes = pd.DataFrame(inputs_for_prd, columns=diabetes_model['features_name'])
    for_diabetes_prd = diabetes_model['model'].predict(df_diabetes)

    if for_diabetes_prd[0]==1:
        return {"prediction" : "Diabetic"}
    else:   
        return {"prediction" : "Not Diabetic"}

@app.post('/predict/breast-cancer')
def breast_cancer_predict(input_data: breast_cancer_inputs):
    inputs_for_prd = np.array([[
        input_data.radius_mean,
        input_data.texture_mean,
        input_data.perimeter_mean,
        input_data.area_mean,
        input_data.smoothness_mean,
        input_data.compactness_mean,
        input_data.concavity_mean,
        input_data.concave_points_mean,
        input_data.symmetry_mean,
        input_data.fractal_dimension_mean,
        input_data.radius_se,
        input_data.texture_se,
        input_data.perimeter_se,
        input_data.area_se,
        input_data.smoothness_se,
        input_data.compactness_se,
        input_data.concavity_se,
        input_data.concave_points_se,
        input_data.symmetry_se,
        input_data.fractal_dimension_se,
        input_data.radius_worst,
        input_data.texture_worst,
        input_data.perimeter_worst,
        input_data.area_worst, 
        input_data.smoothness_worst,
        input_data.compactness_worst,
        input_data.concavity_worst,
        input_data.concave_points_worst,
        input_data.symmetry_worst,
        input_data.fractal_dimension_worst
    ]])

    df_cancer = pd.DataFrame(inputs_for_prd, columns=breast_cancer_model['features_name'])
    for_breast_cancer_prd = breast_cancer_model['model'].predict(df_cancer)
    if for_breast_cancer_prd[0] == 1:
        return {"prediction" :"Malignant (Cancer Detected)"}
    else:
        return {"prediction" :"Benign (No Cancer)"}