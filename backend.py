import requests

API_KEY = "0ecaafe922ff1501dadc2a365373c38b"

#kind for the type of weather
def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"  #make sure to remove all spaces in url
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

#this conditional block ensures that this get_data call is only triggered when we are executing the script directly
#  and not when the script is being imported from somewhere else

if __name__=="__main__":
    print(get_data(place ="Tokyo", forecast_days=3))
