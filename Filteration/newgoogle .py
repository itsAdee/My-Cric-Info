import requests

url = "https://g-search.p.rapidapi.com/search"

querystring = {"q": "WD parnell espn cricinfo", "location_name": "London,Ontario,Canada",
               "location_parameters_auto": "true"}

headers = {
    "X-RapidAPI-Key": "67c4a6c3f1mshaeb2eeb56f92973p1bcca3jsnf3f40b3493d1",
    "X-RapidAPI-Host": "g-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
# number = response.json()
# number = number['data']['organic_results'][0]['url'].split('-')[-1]
print(response.text)
