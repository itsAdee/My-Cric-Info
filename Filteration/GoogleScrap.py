import requests
from player import Player
from googlesearch import search


def Scrapper(player_name, x):
    # x = int(x)
    # url = "https://google-search72.p.rapidapi.com/search"
    # querystring = {"query": player_name, "gl": "us", "lr": "en",
    #                "num": "10", "start": "0", "sort": "relevance"}
    # my_keys = ['67c4a6c3f1mshaeb2eeb56f92973p1bcca3jsnf3f40b3493d1']
    # x = x % 3
    # # '67c4a6c3f1mshaeb2eeb56f92973p1bcca3jsnf3f40b3493d1',

    # headers = {
    #     "X-RapidAPI-Key": my_keys[0],
    #     "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    # }
    # response = requests.request(
    #     "GET", url, headers=headers, params=querystring)
    # number = response.json()
    # number = number['items'][0]['link'].split('-')[-1]
    url = "https://g-search.p.rapidapi.com/search"
    my_url = player_name + " espn cricinfo"

    querystring = {"q": my_url, "location_name": "London,Ontario,Canada",
                   "location_parameters_auto": "true"}

    headers = {
        "X-RapidAPI-Key": "67c4a6c3f1mshaeb2eeb56f92973p1bcca3jsnf3f40b3493d1",
        "X-RapidAPI-Host": "g-search.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    number = response.json()
    number = number['data']['organic_results'][0]['url'].split('-')[-1]

    return number


def Player_Stats(x):
    current_player = Player(x)
    full_name = current_player.name
    first_name = full_name.split(' ')[0]
    last_name = full_name.split(' ')[1]

    batting_style = current_player.batting_style['description'] if current_player.batting_style else None
    bowling_style = current_player.bowling_style['description'] if current_player.bowling_style else None
    playing_role = current_player.playing_role['name'] if current_player.playing_role else None
    dob = current_player.date_of_birth if current_player.date_of_birth else None
    return first_name, last_name, batting_style, bowling_style, playing_role, dob


search_term = 'ss mechkechnie'
query = search_term + " espn cricinfo"
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    player_id = j.split('-')[-1]
    print(player_id)
