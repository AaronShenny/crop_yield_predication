import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# Load dataset, model, and scaler
df = pd.read_csv("crop_yield_dataset (1).csv")
model = joblib.load("crop_yield_model (1).pkl")
scaler = joblib.load("scaler (1).pkl")  # <-- must be saved from the notebook (see note at bottom)

# Columns that were standardized during training (must match the notebook exactly,
# in the same order used when the scaler was fit)
NUMERICAL_COLS = [
    "Rainfall_mm",
    "Temperature_C",
    "Soil_pH",
    "Fertilizer_kg_per_ha",
    "Pesticide_kg_per_ha",
    "Sunlight_Hours_per_day",
    "Farm_Size_ha",
]

# Full feature order the model expects (must match X.columns from training)
MODEL_FEATURE_ORDER = [
    "Rainfall_mm", "Temperature_C", "Soil_pH", "Fertilizer_kg_per_ha",
    "Pesticide_kg_per_ha", "Sunlight_Hours_per_day", "Farm_Size_ha",
    "Soil_Type_Loamy", "Soil_Type_Peaty", "Soil_Type_Sandy", "Soil_Type_Silty",
    "Crop_Type_Cotton", "Crop_Type_Maize", "Crop_Type_Rice",
    "Crop_Type_Soybean", "Crop_Type_Wheat", "Irrigation_Yes"
]

# Main title
st.title("🌾 Crop Yield Prediction")
st.write("Welcome to the Crop Yield Prediction System!")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Dataset Overview", "EDA Dashboard", "Model Performance", "Prediction"]
)

# Pages
if page == "Home":
    st.header("🏠 Home")
    st.write("This application predicts crop yield based on different agricultural factors.")

elif page == "Dataset Overview":
    st.header("📊 Dataset Overview")

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Number of Rows", df.shape[0])

    with col2:
        st.metric("Number of Columns", df.shape[1])

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Column Names")
    st.write(list(df.columns))

elif page == "EDA Dashboard":
    st.header("📈 EDA Dashboard")

    st.subheader("🌾 Average Crop Yield by Crop Type")

    crop_yield = df.groupby("Crop_Type")["Crop_Yield_tonnes_per_ha"].mean()

    st.bar_chart(crop_yield)

    st.subheader("🌱 Average Crop Yield by Soil Type")

    soil_yield = df.groupby("Soil_Type")["Crop_Yield_tonnes_per_ha"].mean()

    st.bar_chart(soil_yield)

    st.subheader("💧 Average Crop Yield by Irrigation")

    irrigation_yield = df.groupby("Irrigation")["Crop_Yield_tonnes_per_ha"].mean()

    st.bar_chart(irrigation_yield)

    st.subheader("🌧️ Rainfall vs Crop Yield")

    st.scatter_chart(
        df,
        x="Rainfall_mm",
        y="Crop_Yield_tonnes_per_ha"
    )

    st.subheader("🌡️ Temperature vs Crop Yield")

    st.scatter_chart(
        df,
        x="Temperature_C",
        y="Crop_Yield_tonnes_per_ha"
    )

    st.subheader("🧪 Fertilizer vs Crop Yield")

    st.scatter_chart(
        df,
        x="Fertilizer_kg_per_ha",
        y="Crop_Yield_tonnes_per_ha"
    )

elif page == "Model Performance":
    st.header("🤖 Model Performance")

    st.write(
        "The following regression models were evaluated "
        "for crop yield prediction:"
    )

    model_names = [
        "Multiple Linear Regression",
        "Polynomial Regression",
        "Ridge Regression",
        "Lasso Regression",
        "ElasticNet Regression"
    ]

    for name in model_names:
        st.write("✅", name)

    st.subheader("📏 Evaluation Metrics")

    st.write("The models were evaluated using:")

    metrics = [
        "MAE - Mean Absolute Error",
        "MSE - Mean Squared Error",
        "RMSE - Root Mean Squared Error",
        "R² - R-squared"
    ]

    for metric in metrics:
        st.write("•", metric)

elif page == "Prediction":
    st.header("🔮 Crop Yield Prediction")
    st.write("Enter the farm details below to predict crop yield.")

    col1, col2 = st.columns(2)

    with col1:
        rainfall = st.number_input(
            "🌧️ Rainfall (mm)",
            min_value=0.0
        )

        temperature = st.number_input(
            "🌡️ Temperature (°C)",
            min_value=0.0
        )

        soil_ph = st.number_input(
            "🌱 Soil pH",
            min_value=0.0,
            max_value=14.0,
            value=7.0
        )

        fertilizer = st.number_input(
            "🧪 Fertilizer (kg/ha)",
            min_value=0.0
        )

        pesticide = st.number_input(
            "🧴 Pesticide (kg/ha)",
            min_value=0.0
        )

    with col2:
        sunlight = st.number_input(
            "☀️ Sunlight (hours/day)",
            min_value=0.0
        )

        farm_size = st.number_input(
            "🚜 Farm Size (ha)",
            min_value=0.0
        )

        # Include ALL soil/crop categories, including the ones dropped as the
        # baseline during one-hot encoding (Clay, Barley) — selecting them
        # correctly produces all-zero dummy flags below.
        soil_type = st.selectbox(
            "🌱 Soil Type",
            ["Clay", "Loamy", "Peaty", "Sandy", "Silty"]
        )

        crop_type = st.selectbox(
            "🌾 Crop Type",
            ["Barley", "Cotton", "Maize", "Rice", "Soybean", "Wheat"]
        )

        irrigation = st.selectbox(
            "💧 Irrigation",
            ["Yes", "No"]
        )

    if st.button("🔮 Predict Crop Yield"):

        input_data = pd.DataFrame({
            "Rainfall_mm": [rainfall],
            "Temperature_C": [temperature],
            "Soil_pH": [soil_ph],
            "Fertilizer_kg_per_ha": [fertilizer],
            "Pesticide_kg_per_ha": [pesticide],
            "Sunlight_Hours_per_day": [sunlight],
            "Farm_Size_ha": [farm_size],

            "Soil_Type_Loamy": [1 if soil_type == "Loamy" else 0],
            "Soil_Type_Peaty": [1 if soil_type == "Peaty" else 0],
            "Soil_Type_Sandy": [1 if soil_type == "Sandy" else 0],
            "Soil_Type_Silty": [1 if soil_type == "Silty" else 0],

            "Crop_Type_Cotton": [1 if crop_type == "Cotton" else 0],
            "Crop_Type_Maize": [1 if crop_type == "Maize" else 0],
            "Crop_Type_Rice": [1 if crop_type == "Rice" else 0],
            "Crop_Type_Soybean": [1 if crop_type == "Soybean" else 0],
            "Crop_Type_Wheat": [1 if crop_type == "Wheat" else 0],

            "Irrigation_Yes": [1 if irrigation == "Yes" else 0]
        })

        # Scale the numeric columns using the SAME fitted scaler used in training.
        # Without this, the model receives raw values on a totally different
        # scale than it was trained on, producing meaningless predictions.
        input_data[NUMERICAL_COLS] = scaler.transform(input_data[NUMERICAL_COLS])

        # Ensure column order exactly matches what the model was trained on
        input_data = input_data[MODEL_FEATURE_ORDER]

        # Make prediction
        prediction = model.predict(input_data)

        # Get predicted value
        predicted_yield = prediction[0]

        # Display result
        st.subheader("🌾 Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Predicted Yield",
                f"{predicted_yield:.2f} tonnes/ha"
            )

        with col2:
            st.metric(
                "Crop",
                crop_type
            )

        with col3:
            st.metric(
                "Soil Type",
                soil_type
            )

        st.success("✅ Prediction generated successfully!")
        st.subheader("📋 Farm Details")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"🌧️ **Rainfall:** {rainfall} mm")
            st.write(f"🌡️ **Temperature:** {temperature} °C")
            st.write(f"🌱 **Soil pH:** {soil_ph}")
            st.write(f"🧪 **Fertilizer:** {fertilizer} kg/ha")
            st.write(f"🧴 **Pesticide:** {pesticide} kg/ha")

        with col2:
            st.write(f"☀️ **Sunlight:** {sunlight} hours/day")
            st.write(f"🚜 **Farm Size:** {farm_size} ha")
            st.write(f"🌱 **Soil Type:** {soil_type}")
            st.write(f"🌾 **Crop Type:** {crop_type}")
            st.write(f"💧 **Irrigation:** {irrigation}")

        st.subheader("💡 Farming Suggestions")

        if rainfall < 500:
            st.write("🌧️ Rainfall is relatively low. Consider proper irrigation.")

        elif rainfall > 2000:
            st.write("🌧️ Rainfall is relatively high. Make sure the field has proper drainage.")

        else:
            st.write("🌧️ Rainfall level is within a moderate range.")

        if soil_ph < 5.5:
            st.write("🌱 Soil pH is acidic. Consider appropriate soil management.")

        elif soil_ph > 7.5:
            st.write("🌱 Soil pH is alkaline. Consider appropriate soil management.")

        else:
            st.write("🌱 Soil pH is within a moderate range.")

        if irrigation == "No":
            st.write("💧 Consider irrigation if rainfall is insufficient.")

        else:
            st.write("💧 Irrigation is available for this farm.")

        if fertilizer == 0:
            st.write("🧪 No fertilizer was entered. Consider following suitable fertilizer recommendations.")

        else:
            st.write("🧪 Fertilizer input has been provided.")

        st.subheader("📥 Download Prediction Report")

        report = f"""
CROP YIELD PREDICTION REPORT
============================

FARM DETAILS
------------
Rainfall: {rainfall} mm
Temperature: {temperature} °C
Soil pH: {soil_ph}
Fertilizer: {fertilizer} kg/ha
Pesticide: {pesticide} kg/ha
Sunlight: {sunlight} hours/day
Farm Size: {farm_size} ha
Soil Type: {soil_type}
Crop Type: {crop_type}
Irrigation: {irrigation}

PREDICTION RESULT
-----------------
Predicted Crop Yield: {predicted_yield:.2f} tonnes/ha

Generated by Crop Yield Prediction System
"""

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="crop_yield_prediction_report.txt",
            mime="text/plain"
        )