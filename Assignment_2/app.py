import json
import requests
import pytest

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"35.5","lon":"-78.5"}

headers = {
	"X-RapidAPI-Key": "2fe75a8c2fmsh89f9104ed644820p14dde3jsn2a6196255215",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
