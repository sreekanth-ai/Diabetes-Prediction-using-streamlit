# 🩺 Diabetes Prediction Project

<img width="1009" height="556" alt="image" src="https://github.com/user-attachments/assets/530ad590-1eec-437a-9747-cfacb7bb5b28" />


Welcome to the **Diabetes Prediction** project repository! This project develops a **machine learning model** to predict diabetes based on various health-related attributes. The workflow covers **data exploration, preprocessing, feature selection, model training, evaluation**, and **deployment via a Streamlit application**.

---

## 📌 Project Overview

### 1. Introduction
Diabetes is a chronic disease affecting millions worldwide. This project aims to predict diabetes using machine learning models trained on health-related attributes. The prediction system is deployed as an **interactive Streamlit app** for end-users.

### 2. Dataset Description
- **Source & Content**: Dataset contains **100,000 records** with 9 features, including numerical and categorical variables.  
- **Target Variable**: `diabetes` (0 = No, 1 = Yes)  

**Features:**
| Feature | Type | Description |
|---------|------|-------------|
| gender | Categorical | Male, Female |
| age | Numerical | Years |
| hypertension | Binary | 0 = No, 1 = Yes |
| heart_disease | Binary | 0 = No, 1 = Yes |
| smoking_history | Categorical | never, current, formerly, No Info, ever, not current |
| bmi | Numerical | Body Mass Index |
| HbA1c_level | Numerical | Hemoglobin A1c Level |
| blood_glucose_level | Numerical | Blood Glucose Level |
| diabetes | Binary | Target variable |

---

## 🧰 Data Exploration & Preprocessing
- **Data Exploration**: Generated summary statistics and performed initial inspection.  
- **Preprocessing Steps**:
  - Encoded categorical variables.
  - Scaled numerical features using **StandardScaler**.
  - Saved preprocessed data for modeling.

---

## 🔍 Feature Selection
- **Correlation Analysis**: Identified features with strong relationships to the target.  
- **Feature Importance**: Used **Random Forest** to rank features.  
- **Variance Threshold**: All features were retained after analysis.  

---

## 🤖 Model Building & Evaluation
- **Data Preparation**: Split dataset into **training** and **testing** sets.  
- **Class Imbalance Handling**: Applied **SMOTE** to oversample minority class.  
- **Model Training**: Trained **Random Forest Classifier** with hyperparameter tuning via **GridSearchCV**.  
- **Evaluation Metrics**:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-Score  
  - Confusion Matrix  
- **Threshold Adjustment**: Adjusted decision threshold to improve **recall** for diabetic cases.  

---

## 🖥️ Model Deployment using Streamlit
- **Setup**: Install dependencies and ensure the trained model (`diabetes_model.pkl`) is in the working directory.  
- **Application Workflow**:
  1. Import libraries and load the trained model.  
  2. Create a form to capture user input features.  
  3. Preprocess input and make predictions.  
  4. Display prediction results in the Streamlit interface.  

### Launch the App
```bash
streamlit run app.py
