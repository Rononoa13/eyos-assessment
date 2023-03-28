import requests
import json
import configparser

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

config = configparser.ConfigParser()
config.read('config.ini')
# Access the values from the configuration file using the get method
google_api_key =('API_KEYS', 'google_api_key')

headers = {
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": google_api_key,
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response.text)
def test_api_response():
    data = response.json()
    new_data = json.dumps(data, indent=3)
    print(new_data)
    print('Successful')

    # Check that the response is as expected
    assert response.status_code == 200


# Gets the language
def test():
    response = requests.post(url, headers=headers)
    data = response.json()
    print(f'data -> {len(data)}')
    new_data = json.dumps(data, indent=3)
    print(f'data -> {len(new_data)}')

test()

