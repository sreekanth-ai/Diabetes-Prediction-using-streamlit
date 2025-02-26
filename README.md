# Diabetes-Prediction-using-streamlit

Welcome to the Diabetes Prediction project repository! This project aims to develop a machine learning model to predict diabetes based on various health-related attributes. The project involves several stages, including data exploration, preprocessing, model training, evaluation, and deployment via a Streamlit application.

## Project Overview

### 1. Introduction
Diabetes is a chronic disease impacting millions globally. This project focuses on developing a machine learning model to predict diabetes based on health-related attributes. The project involves data exploration, preprocessing, model training, and deployment through a Streamlit application.

### 2. Dataset Description
- **Source and Content**: The dataset contains 100,000 records with 9 features, including both numerical and categorical variables. The target variable indicates whether an individual has diabetes (1) or not (0).
- **Features**:
  - `gender`: Categorical (Male, Female)
  - `age`: Numerical (Years)
  - `hypertension`: Binary (0 = No, 1 = Yes)
  - `heart_disease`: Binary (0 = No, 1 = Yes)
  - `smoking_history`: Categorical (e.g., never, current, formerly, No Info, ever, not current)
  - `bmi`: Numerical (Body Mass Index)
  - `HbA1c_level`: Numerical (Hemoglobin A1c Level)
  - `blood_glucose_level`: Numerical (Blood Glucose Level)
  - `diabetes`: Binary (Target variable, 0 = No, 1 = Yes)

### 3. Data Exploration and Preprocessing
- **Data Exploration**: Initial inspection and summary statistics were generated to understand the dataset.
- **Preprocessing**:
  - **Categorical Encoding**: Encoded categorical variables.
  - **Feature Scaling**: Scaled numerical features using StandardScaler.
  - **Saved Data**: Preprocessed data saved as a CSV file.

### 4. Feature Selection
- **Correlation Analysis**: Identified features with strong relationships to the target variable.
- **Feature Importance**: Used Random Forest to rank features based on importance.
- **Variance Threshold**: Considered but all features were retained.

### 5. Model Building and Evaluation
- **Data Preparation**: Split dataset into training and testing sets.
- **Class Imbalance Handling**: Used SMOTE to oversample the minority class.
- **Model Training**: Random Forest classifier was trained and tuned using GridSearchCV.
- **Evaluation**: Assessed model performance using accuracy, precision, recall, F1-score, and confusion matrix.
- **Threshold Adjustment**: Adjusted decision threshold to improve recall for diabetic cases.

### 6. Model Deployment using Streamlit
- **Setup**: Instructions for setting up and running the Streamlit application.
- **Application Workflow**:
  - Import libraries and load the trained model.
  - Create a form to capture input features.
  - Preprocess input data and make predictions.
  - Display predictions in the Streamlit app.

### 7. Conclusion
The project successfully developed and deployed a machine learning model for diabetes prediction. The Random Forest classifier achieved high accuracy, especially for non-diabetic cases. Future work could enhance the model’s prediction of diabetic cases and deploy the application on a cloud platform for broader accessibility.
