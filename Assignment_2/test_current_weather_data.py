import requests
import configparser

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

# read the configuration file:
config = configparser.ConfigParser()
config.read('config.ini')
# Access the values from the configuration file using the get method
weather_api_key =('API_KEYS', 'weather_api_key')

querystring = {"lon":"38.5","lat":"-78.5"}

headers = {
	"X-RapidAPI-Key": weather_api_key,
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)