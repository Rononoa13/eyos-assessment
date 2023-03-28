import json
import requests
import pytest
import configparser

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/alerts"

# read the configuration file:
config = configparser.ConfigParser()
config.read('config.ini')
# Access the values from the configuration file using the get method
weather_api_key =('API_KEYS', 'weather_api_key')

querystring = {"lat":"35.5","lon":"-78.5"}

headers = {
	"X-RapidAPI-Key": weather_api_key,
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

# valid response when valid input parameters such as latitude, longitude, and API key are provided.
def test_response():
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response)
    data = response.json()
    # print(json.dumps(data, indent=3))
    assert response.status_code == 200

# Test when invalid input parameters such as latitude, longitude, and API key are provided.
def test_invalid_lat_log_test():
    querystring = {"lat":"-500","lon":"-500"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert response.status_code == 200