import requests
import json
import configparser

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

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

response = requests.request("GET", url, headers=headers, params=querystring)

# // print(response.text)
# // Test when valid response when valid input parameters such as latitude, longitude, and API key are provided.
def test_api_response():
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response)
    data = response.json()

    assert response.status_code == 200
    print('Successful Request')
    
def test_api_data_fields():
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    assert len(data) == 7
    print('API returns 7 keys successfully')
    # assert data.keys() in ['timezone', 'data', 'city_name', 'state_code', 'lon', 'country_code', 'lat']

test_api_data_fields()