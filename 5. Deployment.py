import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import VotingClassifier

# Load pre-trained models and preprocessor
def load_models():
    models = {}
    model_names = ["Simple_Decision_Tree", "Tuned_Decision_Tree", "KNN", "Random_Forest", "XGBoost", "Voting_Classifier"]
    for name in model_names:
        with open(f"pickle_files/{name.lower()}_model.pkl", "rb") as file:
            models[name] = pickle.load(file)
    return models

def load_preprocessor():
    with open("pickle_files/preprocessor.pkl", "rb") as file:
        preprocessor = pickle.load(file)
    return preprocessor

models = load_models()
preprocessor = load_preprocessor()

# Preprocess user input
def preprocess_input(data):
    preprocessed_data = preprocessor.transform(data)
    return preprocessed_data

def main():
    st.title("Tanzanian Water Wells Status Prediction")

    # Collect user input
    amount_tsh = st.number_input("Enter the amount_tsh:")
    gps_height = st.number_input("Enter the gps_height:")
    basin = st.selectbox("Select the basin:", ["Lake Nyasa", "Lake Victoria", "Pangani", "Rufiji", "Lake Tanganyika", "Wami / Ruvu"])
    region = st.selectbox("Select the region:", ["Iringa", "Mara", "Manyara", "Mtwara", "Kagera", "Tanga"])
    extraction_type = st.selectbox("Select the extraction_type:", ["gravity", "submersible", "swn 80", "nira/tanira", "india mark ii", "other"])
    water_quality = st.selectbox("Select the water_quality:", ["soft", "salty", "milky", "coloured"])
    quantity = st.selectbox("Select the quantity:", ["enough", "insufficient", "dry", "seasonal", "unknown"])
    payment_type = st.selectbox("Select the payment_type:", ["never pay", "pay per bucket", "pay annually", "pay monthly"])
    management_group = st.selectbox("Select the management_group:", ["user-group", "other", "commercial", "parastatal", "trust"])
    source_type = st.selectbox("Select the source_type:", ["spring", "shallow well", "borehole", "river/lake", "rainwater harvesting", "other"])
    waterpoint_type = st.selectbox("Select the waterpoint_type:", ["communal standpipe", "hand pump", "other", "communal standpipe multiple", "improved spring", "cattle trough"])

    # Preprocess user input
    input_data = pd.DataFrame({
        "amount_tsh": [amount_tsh], 
        "gps_height": [gps_height], 
        "basin": [basin], 
        "region": [region],
        "extraction_type": [extraction_type],
        "water_quality": [water_quality],
        "quantity": [quantity],
        "payment_type": [payment_type],
        "management_group": [management_group],
        "source_type": [source_type],
        "waterpoint_type": [waterpoint_type]
    })
    input_data = preprocess_input(input_data)

    # Make predictions
    prediction = models["Voting_Classifier"].predict(input_data)

    # Decode prediction
    le = LabelEncoder()
    le.classes_ = pickle.load(open("pickle_files/label_encoder.pkl", "rb"))
    prediction_label = le.inverse_transform(prediction)

    # Display prediction
    st.subheader("Prediction:")
    st.write(f"The predicted status_group is: {prediction_label[0]}")

if __name__ == "__main__":
    main()
