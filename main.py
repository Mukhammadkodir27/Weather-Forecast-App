import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")  # max days to be shown
# we cannot change the max value of forecast days as we are using api for weather forecast of 5 days
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# if we add, the graph will be under the subheader
# the figure object for the graph you can get it from a plotting library (data visualization library) such as "Plotly" or "Bokeh"
# before we use plotly_chart, we create plotly figure first

# def get_data(days):
#   dates = ["2022-25-10", "2022-26-10", "2022-27-10"] #just a sample and random date to check the program execution
#   temperatures = [10, 11, 15]
#   temperatures = [days * i for i in temperatures]  #each time we change the date, temperature will be changed
#   return dates, temperatures

if place:  # if place exists
    # Get a temperature/sky data
    try: 
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})  # label is expected to be a dictionary
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear:" "images/clear.png", "Clouds:" "images/cloud.png", "Rain:" "images/rain.png", "Snow:" "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]  # for weather conditions
            image_paths = [images[condition, "default_image.png"] for condition in sky_conditions]
            #print(sky_conditions)
            st.image(image_paths)
    except KeyError:
        st.write("This place does not exist.")
