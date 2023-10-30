import requests
from config_data.config import SiteSattings

site = SiteSattings()


url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Yeisk"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "https://www.weatherapi.com/current.json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())