import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "2fe75a8c2fmsh89f9104ed644820p14dde3jsn2a6196255215",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
print(response)
# print(response.text)


def test_successful_post():
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 200
    print("201 Successfully Created")



def test_successful_post():
    target = 'yo'
    payload = f"q=Hello%2C%20world!&target={target}&source=en"
    print(payload)
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    assert response.status_code == 200
    print("201 Successfully Created")

test_successful_post()