import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to be forecasted")   #max days to be shown 

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
