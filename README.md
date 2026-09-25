# 🌾 Crop Yield Prediction — Final Team Tasks

**Team:** Aaron • Emmanuel • Nofiya • Ganga • Amna  
**Project Type:** Regression + EDA + Streamlit  
**Target:** `Crop_Yield_tonnes_per_ha`

---

# 🔄 Project Workflow

```text
Raw Dataset
    ↓
Aaron — Data Cleaning & Preprocessing
    ↓
Clean Dataset
    ↓
Emmanuel — EDA
    ↓
EDA Findings
    ↓
Nofiya — Feature Engineering & Feature Selection
    ↓
Final Feature Set
    ↓
Ganga — Multiple Linear Regression & Evaluation
    ↓
Final Model
    ↓
Amna — Streamlit & Deployment
```

---

# 👨‍💻 AARON — Data Cleaning & Preprocessing

## 1. Data Understanding

- [X] Load the raw dataset
- [X] Check dataset shape
- [X] Inspect column names
- [X] Check data types
- [X] Understand each feature
- [X] Identify the target variable

## 2. Data Cleaning

- [X] Check missing values
- [X] Check duplicate rows
- [X] Check invalid values
- [X] Check negative/impossible values
- [X] Check numerical ranges
- [X] Check categorical values
- [X] Detect outliers
- [X] Decide how to handle outliers
- [X] Document all cleaning decisions

## 3. Preprocessing

- [ ] Separate features `X` and target `y`
- [X] Identify numerical features
- [X] Identify categorical features
- [X] Encode categorical variables
- [X] Apply required scaling/transformation
- [ ] Perform train/test split
- [X] Prevent data leakage


## 4. Deliverables

- [ ] `01_data_cleaning.ipynb`
- [ ] `preprocessing.py`
- [ ] Cleaned dataset
- [ ] Data-cleaning summary

---

# 📊 EMMANUEL — Exploratory Data Analysis

## 1. Dataset Overview

- [ ] Dataset shape
- [ ] Summary statistics
- [ ] Data types
- [ ] Missing-value analysis
- [ ] Unique-value analysis

## 2. Univariate Analysis

- [ ] Rainfall distribution
- [ ] Temperature distribution
- [ ] Fertilizer distribution
- [ ] Crop-yield distribution
- [ ] Boxplots for numerical variables

## 3. Categorical Analysis

- [ ] Region distribution
- [ ] Soil type distribution
- [ ] Crop type distribution
- [ ] Irrigation distribution

## 4. Relationship Analysis

- [ ] Rainfall vs crop yield
- [ ] Temperature vs crop yield
- [ ] Fertilizer vs crop yield
- [ ] Crop type vs yield
- [ ] Soil type vs yield
- [ ] Region vs yield
- [ ] Irrigation vs yield

## 5. Correlation & Insights

- [ ] Create correlation matrix
- [ ] Identify important relationships
- [ ] Identify possible redundant/highly related features
- [ ] Write 5–10 meaningful EDA findings
- [ ] Select presentation-ready visualizations

## 6. Handoff to Nofiya

- [ ] Share important EDA findings
- [ ] Share useful relationships between variables
- [ ] Point out potentially useful or redundant features

## 7. Deliverables

- [ ] `02_EDA.ipynb`
- [ ] EDA graphs
- [ ] EDA findings
- [ ] Presentation visualizations
- [ ] EDA material for Streamlit

---

# 🧠 NOFIYA — Feature Engineering & Feature Selection

> **Main responsibility:** Turn the EDA findings into a useful final feature set for modelling.

## 1. Review Existing Features

- [ ] Review Aaron's cleaned dataset
- [ ] Review Emmanuel's EDA findings
- [ ] Understand the available numerical and categorical features
- [ ] Identify potentially useful features
- [ ] Identify potentially redundant features

## 2. Feature Engineering

- [ ] Identify meaningful derived features
- [ ] Test rainfall-related derived features
- [ ] Test fertilizer-related derived features
- [ ] Test temperature-related derived features
- [ ] Compare model input before and after feature creation
- [ ] Remove engineered features that do not help
- [ ] Document every engineered feature and its purpose

## 3. Feature Transformation

- [ ] Check numerical feature distributions
- [ ] Identify skewed features where relevant
- [ ] Apply appropriate scaling/transformation where required
- [ ] Compare results before and after transformation
- [ ] Document transformation decisions

## 4. Feature Selection

- [ ] Analyze feature relationships/correlations
- [ ] Check for redundant or highly related features
- [ ] Select relevant features for modelling
- [ ] Compare full feature set vs selected feature set
- [ ] Document why features were retained or removed

## 5. Final Handoff to Ganga

- [ ] Prepare final feature list
- [ ] Document engineered features
- [ ] Document transformations
- [ ] Provide final modelling dataset/input structure

## 6. Deliverables

- [ ] `03_feature_engineering.ipynb`
- [ ] Feature-engineering results
- [ ] Feature-selection results
- [ ] Final feature list
- [ ] Feature-analysis visualizations
- [ ] Feature-engineering summary

---

# 🤖 GANGA — Regression & Model Evaluation

## 1. Model Preparation

- [ ] Receive final feature set from Nofiya
- [ ] Use Aaron's preprocessing pipeline
- [ ] Use the agreed train/test split
- [ ] Prepare training and testing data

## 2. Regression Model

- [ ] Train Multiple Linear Regression
- [ ] Generate Polynomial Regression, Ridge, Lasso, ElasticNet
- [ ] Generate predictions on training data
- [ ] Generate predictions on test data

## 3. Evaluation Metrics

- [ ] Calculate MAE
- [ ] Calculate MSE
- [ ] Calculate RMSE
- [ ] Calculate R² Score

## 4. Model Analysis

- [ ] Compare training vs test performance
- [ ] Check for overfitting
- [ ] Check for underfitting
- [ ] Analyze prediction errors/residuals
- [ ] Perform cross-validation
- [ ] Record cross-validation results

## 5. Feature Set Comparison

- [ ] Evaluate full feature set
- [ ] Evaluate Nofiya's selected feature set
- [ ] Compare performance
- [ ] Document the effect of feature selection

## 6. Final Model

- [ ] Finalize the model using documented criteria
- [ ] Save the final trained model
- [ ] Document model configuration
- [ ] Provide model file to Amna

## 7. Deliverables

- [ ] `04_model_training.ipynb`
- [ ] Model evaluation results
- [ ] Cross-validation results
- [ ] Feature-set comparison
- [ ] Saved final model
- [ ] Final model explanation

---

# 🎨 AMNA — Streamlit & Deployment

## 1. Application Structure

- [ ] Create Streamlit project
- [ ] Create Home page
- [ ] Create Dataset Overview page
- [ ] Create EDA page
- [ ] Create Model Results page
- [ ] Create Prediction page

## 2. Dataset Overview

- [ ] Show dataset size
- [ ] Show feature names
- [ ] Show target variable
- [ ] Show dataset preview
- [ ] Show feature descriptions

## 3. EDA Dashboard

- [ ] Add crop-yield distribution
- [ ] Add crop comparison
- [ ] Add region comparison
- [ ] Add soil comparison
- [ ] Add irrigation comparison
- [ ] Add rainfall vs yield
- [ ] Add temperature vs yield
- [ ] Add fertilizer vs yield

## 4. Model Results

- [ ] Display model information
- [ ] Display MAE
- [ ] Display MSE
- [ ] Display RMSE
- [ ] Display R²
- [ ] Display cross-validation results

## 5. Prediction Page

### Inputs

- [ ] Region
- [ ] Soil type
- [ ] Crop type
- [ ] Rainfall
- [ ] Temperature
- [ ] Fertilizer
- [ ] Irrigation

### Prediction Flow

```text
User Input
    ↓
Preprocessing Pipeline
    ↓
Feature Engineering / Transformation
    ↓
Final Model
    ↓
Predicted Crop Yield
```

- [ ] Add input validation
- [ ] Load preprocessing pipeline
- [ ] Load saved model
- [ ] Apply required feature transformations
- [ ] Generate prediction
- [ ] Display predicted yield in tonnes/ha

## 6. Deployment

- [ ] Create `requirements.txt`
- [ ] Test application locally
- [ ] Connect final model
- [ ] Connect preprocessing pipeline
- [ ] Test prediction flow
- [ ] Fix deployment issues
- [ ] Deploy to Streamlit Community Cloud
- [ ] Test public URL
- [ ] Share working application link

## 7. Deliverables

- [ ] `streamlit_app.py`
- [ ] `requirements.txt`
- [ ] Streamlit application
- [ ] Public application URL

---

# 📚 REPORT — TEAM

- [ ] Title
- [ ] Abstract
- [ ] Introduction
- [ ] Problem Statement
- [ ] Objectives
- [ ] Dataset Description
- [ ] Data Cleaning
- [ ] Exploratory Data Analysis
- [ ] Feature Engineering
- [ ] Feature Selection
- [ ] Methodology
- [ ] Regression Model
- [ ] Evaluation Metrics
- [ ] Cross-Validation
- [ ] Results
- [ ] Model Analysis
- [ ] Streamlit Application
- [ ] Deployment
- [ ] Limitations
- [ ] Future Scope
- [ ] Conclusion
- [ ] References

---

# 🎤 PRESENTATION — TEAM

- [ ] Title slide
- [ ] Team members
- [ ] Problem statement
- [ ] Objectives
- [ ] Dataset
- [ ] Data-cleaning process
- [ ] EDA findings
- [ ] Important visualizations
- [ ] Feature engineering
- [ ] Feature selection
- [ ] Regression methodology
- [ ] Evaluation metrics
- [ ] Model results
- [ ] Overfitting/underfitting analysis
- [ ] Streamlit application
- [ ] Live prediction demonstration
- [ ] Deployment
- [ ] Conclusion

---

# 🔗 TEAM HANDOFF CHECKLIST

## Aaron → Emmanuel

- [ ] Cleaned dataset shared
- [ ] Data-cleaning decisions documented

## Emmanuel → Nofiya

- [ ] EDA notebook shared
- [ ] Important relationships shared
- [ ] Important findings shared
- [ ] Potentially useful/redundant features identified

## Nofiya → Ganga

- [ ] Final feature list shared
- [ ] Engineered features documented
- [ ] Transformations documented
- [ ] Final input structure shared

## Ganga → Amna

- [ ] Final model saved
- [ ] Model metrics shared
- [ ] Final feature order shared
- [ ] Preprocessing/model loading instructions shared

## Amna → Team

- [ ] Streamlit app working locally
- [ ] Prediction flow working
- [ ] Deployment completed
- [ ] Public URL tested

---

# ✅ FINAL TEAM CHECK

- [ ] All notebooks completed
- [ ] All outputs saved
- [ ] Preprocessing and model pipeline tested end-to-end
- [ ] Final feature order verified
- [ ] Final model verified
- [ ] Streamlit prediction verified
- [ ] Report completed
- [ ] Presentation completed
- [ ] GitHub repository cleaned and organized
- [ ] Final application URL tested

---

## 📌 Important Scope Note

This project plan stays focused on the concepts covered in the training material: data cleaning, preprocessing, feature engineering, feature selection, feature transformation, data splitting, linear/multiple linear regression, evaluation, cross-validation, and overfitting/underfitting.

Advanced techniques such as **RFE, VIF, Ridge, Lasso, ElasticNet, and extensive hyperparameter tuning are not mandatory in this final task plan** unless the instructor separately requires them.
