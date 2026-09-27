import joblib
import pandas as pd
import streamlit as st

# Ensure custom transformer classes are importable during unpickling
import model_pipeline  # noqa: F401

st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾", layout="wide")

DATA_PATH = "crop_yield_dataset.csv"
MODEL_PATH = "crop_yield_model.pkl"


df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

st.title("🌾 Crop Yield Prediction")
st.write("Predict crop yield (tonnes/ha) from raw farm inputs.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dataset Overview", "EDA Dashboard", "Prediction"])

if page == "Home":
    st.header("🏠 Home")
    st.write("This app uses one serialized end-to-end pipeline for preprocessing and prediction.")

elif page == "Dataset Overview":
    st.header("📊 Dataset Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Missing Values")
    st.dataframe(df.isna().sum().rename("missing_count"))

elif page == "EDA Dashboard":
    st.header("📈 EDA Dashboard (Pre-encoding)")

    st.subheader("Average Yield by Crop Type")
    st.bar_chart(df.groupby("Crop_Type", dropna=False)["Crop_Yield_tonnes_per_ha"].mean())

    st.subheader("Average Yield by Soil Type")
    st.bar_chart(df.groupby("Soil_Type", dropna=False)["Crop_Yield_tonnes_per_ha"].mean())

    st.subheader("Average Yield by Irrigation")
    st.bar_chart(df.groupby("Irrigation", dropna=False)["Crop_Yield_tonnes_per_ha"].mean())

    st.subheader("Rainfall vs Crop Yield")
    st.scatter_chart(df, x="Rainfall_mm", y="Crop_Yield_tonnes_per_ha")

elif page == "Prediction":
    st.header("🔮 Crop Yield Prediction")

    col1, col2 = st.columns(2)
    with col1:
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=950.0)
        temperature = st.number_input("Temperature (°C)", min_value=0.0, value=27.0)
        soil_ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
        fertilizer = st.number_input("Fertilizer (kg/ha)", min_value=0.0, value=190.0)
        pesticide = st.number_input("Pesticide (kg/ha)", min_value=0.0, value=4.0)

    with col2:
        sunlight = st.number_input("Sunlight (hours/day)", min_value=0.0, value=8.0)
        farm_size = st.number_input("Farm Size (ha)", min_value=0.0, value=60.0)
        soil_type = st.selectbox("Soil Type", sorted(df["Soil_Type"].dropna().unique().tolist()))
        crop_type = st.selectbox("Crop Type", sorted(df["Crop_Type"].dropna().unique().tolist()))
        irrigation = st.selectbox("Irrigation", sorted(df["Irrigation"].dropna().unique().tolist()))

    if st.button("Predict"):
        input_data = pd.DataFrame(
            {
                "Soil_Type": [soil_type],
                "Crop_Type": [crop_type],
                "Rainfall_mm": [rainfall],
                "Temperature_C": [temperature],
                "Soil_pH": [soil_ph],
                "Fertilizer_kg_per_ha": [fertilizer],
                "Pesticide_kg_per_ha": [pesticide],
                "Sunlight_Hours_per_day": [sunlight],
                "Farm_Size_ha": [farm_size],
                "Irrigation": [irrigation],
            }
        )

        prediction = float(model.predict(input_data)[0])
        st.metric("Predicted Yield", f"{prediction:.2f} tonnes/ha")
        st.success("Prediction generated using the trained end-to-end pipeline.")
