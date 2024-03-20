# --------------------------------------
# Open Weathermap API
# https://https://docs.openweather.co.uk/api
# ****** Remove the API Key and Custom Search Engine Key before sharing
# --------------------------------------
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# --------------------------------------

# Import Libraries
# --------------------------------------
import requests
from pprint import pprint

# Set up variables
# --------------------------------------
urlLocation = "http://api.openweathermap.org/geo/1.0/direct?"
urlWeather = "https://api.openweathermap.org/data/2.5/weather?"

# Obtain the API Key
# --------------------------------------
txtAPIKey = input("Enter the API Key : ")

# Obtain the location
# Currently limited to 1 response and no error handling if there is no location found
# --------------------------------------
txtCity = input("Enter the City name (eg Melbourne) : ")
txtCountryCode = input("Enter the Country Code (eg AU) : ")
reqLocationData = urlLocation + "q=" + txtCity + ",," + txtCountryCode + "&limit=1&appid=" + txtAPIKey
jsoLocationData = requests.get(reqLocationData).json()
txtLat = str(jsoLocationData[0]['lat'])
txtLon = str(jsoLocationData[0]['lon'])

# Obtain the weather for the location
# --------------------------------------
reqWeatherData = urlWeather + "units=metric&appid=" + txtAPIKey + "&lat=" + txtLat + "&lon=" + txtLon
jsoWeatherData = requests.get(reqWeatherData).json()
txtTemp = jsoWeatherData['main']['temp']
txtDescription = jsoWeatherData['weather'][0]['description']

# Printthe weather
print("-----------------------------------------")
print("Weather Data :\n")
print('Temperature : ', txtTemp)
print('Description : ', txtDescription)
print("-----------------------------------------")
pprint(jsoWeatherData)
print("-----------------------------------------")
