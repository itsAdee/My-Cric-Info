import sys
import os
from pathlib import Path
import json
import pandas as pd
import random
from Filtering_Players import extract_playerInfo
from Series_MatchInfo import extract_matchinfo, extract_series_info, insert_series_info, insert_match_info
from ExtractBallInformation import extractballinfo, InsertBallInfo, extract_batterInfo, extract_bowlerInfo
from ExtractWicketInfromation import extractwicketinfo, InsertWicketInfo


def FindParticularMatches(title, season):
    currentPath = Path.cwd()
    list = []
    match_directory = currentPath / "Matches"
    for file in os.listdir(match_directory):
        if file.endswith(".json"):
            id = file.split(".")[0]
            try:
                myfile = open("Matches//"+str(id)+".json", "r")
                json_data = json.loads(myfile.read())
                event_name = json_data['info']['event']['name']
                event_season = json_data['info']['season']
                if event_name == title and event_season == season:
                    list.append(id)
            except:
                continue
    return list


my_matches = FindParticularMatches("England tour of Pakistan", '2022')
# my_matches = ['1298150', '1298158', '1298163', '1298163',
#               '1298170', '1298175', '1298177', '1298179']
print(my_matches)

extract_playerInfo(my_matches)
insert_series_info(my_matches)
insert_match_info(my_matches)

InsertBallInfo(my_matches)
InsertWicketInfo(my_matches)
