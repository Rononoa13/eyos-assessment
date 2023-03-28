import requests
import configparser

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

config = configparser.ConfigParser()
config.read('config.ini')
# Access the values from the configuration file using the get method
google_api_key =('API_KEYS', 'google_api_key')

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": google_api_key,
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
# print(response)
# print(response.text)


def test_successful_post():
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 200
    print("201 Successfully Created")



def test_successful_post():
    target = 'ne'
    payload = f"q=Hello%2C%20world!&target={target}&source=en"
    print(payload)
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    assert response.status_code == 200
    print("201 Successfully Created")


# No target
def test_unsuccessful_post():
    target = 'nep'
    payload = f"q=Hello%2C%20world!&target={target}&source=en"
    print(payload)
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    assert response.status_code == 400
    print("201 Successfully Created")

