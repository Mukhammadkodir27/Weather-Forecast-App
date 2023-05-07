import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place : ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to be forecasted")   #max days to be shown 

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

#if we add, the graph will be under the subheader
#the figure object for the graph you can get it from a plotting library (data visualization library) such as "Plotly" or "Bokeh"
#before we use plotly_chart, we create plotly figure first 

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"] #just a sample and random date to check the program execution
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]  #each time we change the date, temperature will be changed
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"}) 
                          #x for dates, y for temperature, x and y should be array type objects, label is exp to be a dictionary 
st.plotly_chart(figure)
