
import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# Load model
model_path = hf_hub_download(
    repo_id="lokeshathipatla/tourism-randomforest-model",
    filename="model.pkl"
)

model = joblib.load(model_path)

st.title("Tourism Package Prediction")

Age = st.number_input("Age", 18, 100, 30)
TypeofContact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
CityTier = st.selectbox("City Tier", [1, 2, 3])
DurationOfPitch = st.number_input("Duration Of Pitch", 1, 1000, 30)

Occupation = st.selectbox(
    "Occupation",
    ["Salaried", "Small Business", "Large Business", "Free Lancer"]
)

Gender = st.selectbox("Gender", ["Male", "Female"])

NumberOfPersonVisiting = st.number_input(
    "Number Of Persons Visiting",
    1, 10, 2
)

NumberOfFollowups = st.number_input(
    "Number Of Followups",
    0, 10, 2
)

ProductPitched = st.selectbox(
    "Product Pitched",
    ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"]
)

PreferredPropertyStar = st.selectbox(
    "Preferred Property Star",
    [1, 2, 3, 4, 5]
)

MaritalStatus = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

NumberOfTrips = st.number_input(
    "Number Of Trips",
    0, 20, 2
)

Passport = st.selectbox("Passport", [0, 1])

PitchSatisfactionScore = st.slider(
    "Pitch Satisfaction Score",
    1, 5, 3
)

OwnCar = st.selectbox("Own Car", [0, 1])

NumberOfChildrenVisiting = st.number_input(
    "Children Visiting",
    0, 10, 0
)

Designation = st.selectbox(
    "Designation",
    ["Manager", "Senior Manager", "AVP", "VP"]
)

MonthlyIncome = st.number_input(
    "Monthly Income",
    1000, 500000, 30000
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Age":[Age],
        "TypeofContact":[TypeofContact],
        "CityTier":[CityTier],
        "DurationOfPitch":[DurationOfPitch],
        "Occupation":[Occupation],
        "Gender":[Gender],
        "NumberOfPersonVisiting":[NumberOfPersonVisiting],
        "NumberOfFollowups":[NumberOfFollowups],
        "ProductPitched":[ProductPitched],
        "PreferredPropertyStar":[PreferredPropertyStar],
        "MaritalStatus":[MaritalStatus],
        "NumberOfTrips":[NumberOfTrips],
        "Passport":[Passport],
        "PitchSatisfactionScore":[PitchSatisfactionScore],
        "OwnCar":[OwnCar],
        "NumberOfChildrenVisiting":[NumberOfChildrenVisiting],
        "Designation":[Designation],
        "MonthlyIncome":[MonthlyIncome]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("Customer is likely to purchase the package")
    else:
        st.error("Customer is unlikely to purchase the package")
