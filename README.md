# 🌾 Crop Yield Prediction — Team TODO

**Team:** Aaron • Emmanuel • Nofiya • Ganga • Amna  
**Project Type:** Regression + EDA + Streamlit  
**Target:** `Crop_Yield_tonnes_per_ha`

---

# 👥 Team Task Breakdown

## 👨‍💻 AARON — Data Cleaning & Preprocessing

### Data Understanding
- [ ] Load the raw dataset
- [ ] Check dataset shape
- [ ] Inspect column names
- [ ] Check data types
- [ ] Understand each feature
- [ ] Identify the target variable

### Data Cleaning
- [ ] Check missing values
- [ ] Check duplicate rows
- [ ] Check invalid values
- [ ] Check negative/impossible values
- [ ] Check numerical ranges
- [ ] Check categorical values
- [ ] Detect outliers
- [ ] Decide how to handle outliers
- [ ] Document all cleaning decisions

### Preprocessing
- [ ] Separate features `X` and target `y`
- [ ] Identify numerical features
- [ ] Identify categorical features
- [ ] Encode categorical features
- [ ] Perform train/test split
- [ ] Apply scaling where required
- [ ] Prevent data leakage
- [ ] Build reusable preprocessing pipeline
- [ ] Save processed dataset

### Deliverables
- [ ] `01_data_cleaning.ipynb`
- [ ] `preprocessing.py`
- [ ] Cleaned dataset
- [ ] Data-cleaning summary

---

# 📊 EMMANUEL — Exploratory Data Analysis

## Dataset Overview
- [ ] Dataset shape
- [ ] Summary statistics
- [ ] Data types
- [ ] Missing-value visualization
- [ ] Unique-value analysis

## Univariate Analysis
- [ ] Rainfall distribution
- [ ] Temperature distribution
- [ ] Fertilizer distribution
- [ ] Crop-yield distribution
- [ ] Boxplots for numerical variables

## Categorical Analysis
- [ ] Region distribution
- [ ] Soil type distribution
- [ ] Crop type distribution
- [ ] Irrigation distribution

## Relationship Analysis
- [ ] Rainfall vs crop yield
- [ ] Temperature vs crop yield
- [ ] Fertilizer vs crop yield
- [ ] Crop type vs yield
- [ ] Soil type vs yield
- [ ] Region vs yield
- [ ] Irrigation vs yield

## Correlation & Insights
- [ ] Correlation matrix
- [ ] Identify strongly related features
- [ ] Identify possible multicollinearity
- [ ] Write 5–10 meaningful EDA findings
- [ ] Select presentation-ready visualizations

### Deliverables
- [ ] `02_EDA.ipynb`
- [ ] EDA graphs
- [ ] EDA findings
- [ ] Visualizations for presentation
- [ ] EDA section for Streamlit

---

# 🧠 NOFIYA — Feature Engineering & RFE

## Feature Engineering
- [ ] Review existing features
- [ ] Identify useful derived features
- [ ] Test rainfall-related features
- [ ] Test fertilizer-related features
- [ ] Test temperature-related features
- [ ] Check whether engineered features improve performance
- [ ] Remove unnecessary engineered features

## Feature Selection
- [ ] Analyze feature correlation
- [ ] Check multicollinearity
- [ ] Calculate VIF where appropriate
- [ ] Run RFE
- [ ] Identify selected features
- [ ] Record RFE rankings
- [ ] Compare full feature set vs RFE feature set

## Analysis
- [ ] Generate feature-importance analysis where applicable
- [ ] Document why selected features were retained
- [ ] Provide final feature list to Ganga

### Deliverables
- [ ] `03_feature_engineering.ipynb`
- [ ] Feature-engineering results
- [ ] RFE results
- [ ] Selected feature list
- [ ] Feature-analysis visuals

---

# 🤖 GANGA — Regression Models & Evaluation

## Required Models
- [ ] Multiple Linear Regression
- [ ] Polynomial Regression
- [ ] Ridge Regression
- [ ] Lasso Regression
- [ ] ElasticNet Regression
- [ ] RFE + Regression

## Model Preparation
- [ ] Use the agreed preprocessing pipeline
- [ ] Use the same train/test split
- [ ] Train all models consistently
- [ ] Record training and test performance

## Evaluation
- [ ] MAE
- [ ] MSE
- [ ] RMSE
- [ ] R² Score

## Cross-Validation
- [ ] Perform 5-fold cross-validation
- [ ] Record mean CV score
- [ ] Record score variation

## Hyperparameter Tuning
- [ ] Tune Polynomial Regression degree
- [ ] Tune Ridge `alpha`
- [ ] Tune Lasso `alpha`
- [ ] Tune ElasticNet `alpha`
- [ ] Tune ElasticNet `l1_ratio`
- [ ] Compare tuned vs default models

## Model Comparison
- [ ] Create final comparison table
- [ ] Compare MAE
- [ ] Compare RMSE
- [ ] Compare R²
- [ ] Check overfitting
- [ ] Select final model based on documented criteria

## Optional Extra
- [ ] Train Random Forest Regressor or Gradient Boosting Regressor
- [ ] Compare nonlinear model with linear models

### Deliverables
- [ ] `04_model_training.ipynb`
- [ ] Model comparison table
- [ ] Cross-validation results
- [ ] Hyperparameter results
- [ ] Saved final model
- [ ] Final model explanation

---

# 🎨 AMNA — Streamlit & Deployment

## Application Structure
- [ ] Create Streamlit project
- [ ] Create Home page
- [ ] Create Dataset Overview page
- [ ] Create EDA page
- [ ] Create Model Comparison page
- [ ] Create Prediction page

## Dataset Page
- [ ] Show dataset size
- [ ] Show feature names
- [ ] Show target variable
- [ ] Show dataset preview
- [ ] Show feature descriptions

## EDA Dashboard
- [ ] Add yield distribution
- [ ] Add crop comparison
- [ ] Add region comparison
- [ ] Add soil comparison
- [ ] Add irrigation comparison
- [ ] Add rainfall vs yield
- [ ] Add temperature vs yield
- [ ] Add fertilizer vs yield

## Model Comparison
- [ ] Display model names
- [ ] Display MAE
- [ ] Display RMSE
- [ ] Display R²
- [ ] Highlight final selected model

## Prediction
- [ ] Region input
- [ ] Soil type input
- [ ] Crop type input
- [ ] Rainfall input
- [ ] Temperature input
- [ ] Fertilizer input
- [ ] Irrigation input
- [ ] Input validation
- [ ] Load preprocessing pipeline
- [ ] Load saved model
- [ ] Generate prediction
- [ ] Display predicted yield in tonnes/ha

## Deployment
- [ ] Create `requirements.txt`
- [ ] Test application locally
- [ ] Fix deployment issues
- [ ] Deploy to Streamlit Community Cloud
- [ ] Test public URL
- [ ] Share working application link

### Deliverables
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
- [ ] RFE
- [ ] Methodology
- [ ] Regression Models
- [ ] Evaluation Metrics
- [ ] Results
- [ ] Model Comparison
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
- [ ] Feature engineering
- [ ] RFE
- [ ] Regression models
- [ ] Evaluation metrics
- [ ] Model comparison
- [ ] Final model
- [ ] Streamlit application
- [ ] Live/demo screenshots
- [ ] Results
- [ ] Conclusion
- [ ] Future scope

---

# 🔧 FINAL INTEGRATION

- [ ] All notebooks run without errors
- [ ] No hard-coded local paths
- [ ] Preprocessing is reproducible
- [ ] Same preprocessing is used during training and prediction
- [ ] No data leakage
- [ ] Final model is saved correctly
- [ ] Streamlit loads the correct model
- [ ] Streamlit uses the correct preprocessing pipeline
- [ ] Test valid inputs
- [ ] Test invalid inputs
- [ ] Test missing inputs
- [ ] Test extreme values
- [ ] Check prediction output
- [ ] Check model metrics
- [ ] Check Streamlit deployment
- [ ] README completed
- [ ] Installation instructions added
- [ ] Dataset source added
- [ ] Model methodology documented
- [ ] Streamlit link added
- [ ] Team contributions documented

---

# 📁 Recommended GitHub Structure

```text
crop-yield-ml/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── models.py
├── models/
│   └── final_model.pkl
├── app/
│   └── streamlit_app.py
├── reports/
├── requirements.txt
└── README.md
```

---

# 📈 PROJECT TRACKER

| Task | Owner | Status |
|---|---|---|
| Dataset audit | Aaron | ☐ |
| Data cleaning | Aaron | ☐ |
| Preprocessing pipeline | Aaron | ☐ |
| EDA | Emmanuel | ☐ |
| EDA insights | Emmanuel | ☐ |
| EDA Streamlit section | Emmanuel + Amna | ☐ |
| Feature engineering | Nofiya | ☐ |
| RFE | Nofiya | ☐ |
| Feature analysis | Nofiya | ☐ |
| Linear Regression | Ganga | ☐ |
| Polynomial Regression | Ganga | ☐ |
| Ridge | Ganga | ☐ |
| Lasso | Ganga | ☐ |
| ElasticNet | Ganga | ☐ |
| RFE + Regression | Ganga | ☐ |
| Cross-validation | Ganga | ☐ |
| Hyperparameter tuning | Ganga | ☐ |
| Model comparison | Ganga | ☐ |
| Streamlit UI | Amna | ☐ |
| Streamlit integration | Amna + Aaron | ☐ |
| Deployment | Amna | ☐ |
| Report | Everyone | ☐ |
| Presentation | Everyone | ☐ |
| Final testing | Everyone | ☐ |

---

# 🚦 Recommended Order

1. **Aaron** → Data Cleaning
2. **Emmanuel** → EDA
3. **Nofiya** → Feature Engineering + RFE
4. **Ganga** → Models + Evaluation
5. **Amna** → Streamlit Integration + Deployment
6. **Everyone** → Report + Presentation + Final Testing

## Definition of Done

- [ ] Clean dataset finalized
- [ ] EDA completed with written findings
- [ ] Feature engineering documented
- [ ] RFE completed
- [ ] All required regression models trained
- [ ] Models evaluated using MAE, MSE, RMSE and R²
- [ ] Cross-validation/tuning completed
- [ ] Final model selected and saved
- [ ] Streamlit application works
- [ ] Application deployed
- [ ] Working link tested
- [ ] Report finalized
- [ ] Presentation finalized
- [ ] GitHub repository clean and reproducible
