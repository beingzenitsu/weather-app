import pyttsx3
import requests
import json

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get city name from user
city = input("Enter city name: ")
api_key = "40527cbbfe6269dcc74da956b3b1f803"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"

# Fetch weather data
r = requests.get(url)
wdic = json.loads(r.text)

# Extract weather details
weather_main = wdic["weather"][0]["main"]
temp = wdic["main"]["temp"]
feels_like = wdic["main"]["feels_like"]
temp_min = wdic["main"]["temp_min"]
temp_max = wdic["main"]["temp_max"]
pressure = wdic["main"]["pressure"]
humidity = wdic["main"]["humidity"]
wind_speed = wdic["wind"]["speed"]
wind_deg = wdic["wind"]["deg"]
clouds = wdic["clouds"]["all"]
sunrise = wdic["sys"]["sunrise"]
sunset = wdic["sys"]["sunset"]
timezone = wdic["timezone"]

# Create speech text
speech_text = (f"Weather in {city}: {weather_main}. "
               f"Current temperature is {temp} degrees celcius . "
               f"It feels like {feels_like} degrees. "
               f"Temperature ranges from {temp_min} to {temp_max} degrees. "
               f"Pressure is {pressure} hPa. "
               f"Humidity is {humidity} percent. "
               f"Wind speed is {wind_speed} meters per second, coming from {wind_deg} degrees. "
               f"Cloudiness is {clouds} percent. "
               f"Sunrise at {sunrise} and sunset at {sunset}. "
               f"Timezone is {timezone}.")

# Print and speak the weather information
print(speech_text)
engine.say(speech_text)
engine.runAndWait()

