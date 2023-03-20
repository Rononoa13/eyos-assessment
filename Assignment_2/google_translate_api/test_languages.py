import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "2fe75a8c2fmsh89f9104ed644820p14dde3jsn2a6196255215",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response.text)
def test_successful_connection():
    assert response.status_code == 200
    data = response.json()
    new_data = json.dumps(data, indent=3)
    print(new_data)
    print('Successful')



def test():
    response = requests.post(url, headers=headers)
    data = response.json()
    new_data = json.dumps(data, indent=3)
    print(new_data)


