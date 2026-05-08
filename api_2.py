        input_data = pd.DataFrame([[
            float(Age), float(Sex), float(cp), float(trestbps), float(chol),
            float(fbs), float(restecg), float(thalach), float(exang),
            float(oldpeak), float(slope), float(ca), float(thal)]], columns=[
            "age","sex","cp","trestbps","chol","fbs",
            "restecg","thalach","exang","oldpeak",
            "slope","ca","thal"
])
       
 result = heart_model.predict(input_data)
        if result[0] == 1:
            heart_result = "Defective Heart"
        else:
            heart_result = "Healthy Heart"
        




diab_df = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi_diabetes, DiabetesPedigreeFunction, Age]],  
        columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])

        prd_diabetes = diabetes_model.predict(diab_df)

        if prd_diabetes[0]==0:
            diabetes_result = "Non_Diabetic"
        else:
            diabetes_result = "Diabetic"
    
    st.success(diabetes_result)




     input_data = pd.DataFrame([[ 
            float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean), float(smoothness_mean),
            float(compactness_mean), float(concavity_mean), float(concave_points_mean), float(symmetry_mean), float(fractal_dimension_mean),
            float(radius_se), float(texture_se), float(perimeter_se), float(area_se), float(smoothness_se),
            float(compactness_se), float(concavity_se), float(concave_points_se), float(symmetry_se), float(fractal_dimension_se),
            float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst), float(smoothness_worst),
            float(compactness_worst), float(concavity_worst), float(concave_points_worst), float(symmetry_worst), float(fractal_dimension_worst)
        ]], columns=[
            'radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean',
            'compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean',
            'radius_se','texture_se','perimeter_se','area_se','smoothness_se',
            'compactness_se','concavity_se','concave points_se','symmetry_se','fractal_dimension_se',
            'radius_worst','texture_worst','perimeter_worst','area_worst','smoothness_worst',
            'compactness_worst','concavity_worst','concave points_worst','symmetry_worst','fractal_dimension_worst'
        ])

        result = breast_cancer_model.predict(input_data)

        if result[0] == 1:
            cancer_result = "Malignant (Cancer Detected)"
        else:
            cancer_result = "Benign (No Cancer)"

    st.success(cancer_result)
