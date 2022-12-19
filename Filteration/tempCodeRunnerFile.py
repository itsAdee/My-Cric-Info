
import requests

url = "https://google-search-2.p.rapidapi.com/organicResults"

querystring = {"query":"P nissanka espn cricinfo","num":"10","gl":"us","hl":"en","page":"0","nfpr":"0","device":"desktop"}

headers = {
	"X-RapidAPI-Key": "bde94c942fmsh5b4416bfd8affc3p19da36jsn751bd5c93def",
	"X-RapidAPI-Host": "google-search-2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)