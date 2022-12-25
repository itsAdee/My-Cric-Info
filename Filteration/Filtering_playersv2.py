import json
import pandas as pd
import random
from GoogleScrap import Scrapper, Player_Stats
from player import Player
from googlesearch import search


def extract_playerInfo(matchlist):
    for match_id in matchlist:
        player_db = pd.read_csv('Filtered_Players.csv')
        new_data_frame = pd.read_csv('Playerdatabasev2.csv')
        file = open("Matches//"+str(match_id)+".json", "r")
        json_data = json.loads(file.read())
        for team, players in json_data['info']['players'].items():
            i = 1
            for player in players:
                print(player)
                if (player not in new_data_frame['Scrapped Name'].values):
                    if (player in player_db['NAME'].values):
                        my_series = player_db.loc[player_db['NAME'] == player]
                        my_series = my_series.iloc[0]
                        first_name = my_series['NAME'].split(' ')[0]
                        last_name = my_series['NAME'].split(' ')[1]
                        date_of_birth = my_series['Birthdate']
                        id = my_series['ID']
                        country = team
                        bowling_style = my_series['Bowling style']
                        batting_style = my_series['Batting style']
                        alive = my_series['Died']
                        new_data_frame.loc[len(new_data_frame.index)] = [id, first_name, last_name, player, team, date_of_birth,
                                                                         alive, batting_style, bowling_style, i]
                    else:
                        search_term = player
                        query = search_term + " espn cricinfo"
                        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                            player_id = j.split('-')[-1]
                            break
                        first_name, last_name, batting_style, bowling_style, playing_role, date_of_birth = Player_Stats(
                            player_id)
                        new_data_frame.loc[len(new_data_frame.index)] = [player_id, first_name, last_name, player, team, date_of_birth,
                                                                         'Alive', batting_style, bowling_style, i]
                    i += 1
                    new_data_frame.to_csv('Playerdatabasev2.csv', index=False)


extract_playerInfo(['1298150', '1298158', '1298163',
                   '1298170', '1298175', '1298177', '1298179'])
