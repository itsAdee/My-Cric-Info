import json
import pandas as pd
import random


def extract_matchinfo(match_id):
    match_file = open("Matches//"+str(match_id)+".json", "r")
    json_data = json.loads(match_file.read())
    match_id = match_id
    match_type = json_data['info']['match_type']
    match_date = json_data['info']['dates'][0]
    event_name = json_data['info']['event']['name']
    winner_team = json_data['info']['outcome']['winner']
    try:
        event_stage = json_data['info']['event']['stage']
    except:
        event_stage = None
    field_umpires_1 = json_data['info']['officials']['umpires'][0]
    field_umpires_2 = json_data['info']['officials']['umpires'][1]
    tv_umpire = json_data['info']['officials']['tv_umpires'][0]

    try:

        result_description = json_data['info']['outcome']['by']['runs']
        result_description = winner_team + " won by  " + \
            str(result_description) + " runs"
    except:

        result_description = json_data['info']['outcome']['by']['wickets']
        result_description = winner_team + " won by  " + \
            str(result_description) + " wickets"

    player_of_match = json_data['info']['player_of_match'][0]
    season = json_data['info']['season']
    team_type = json_data['info']['team_type']
    team_1 = json_data['info']['teams'][0]
    team_2 = json_data['info']['teams'][1]
    return match_id, match_type, match_date, event_name, event_stage, field_umpires_1, field_umpires_2, tv_umpire, winner_team, result_description, player_of_match, season, team_type, team_1, team_2


def extract_series_info(match_id):
    print(match_id)
    match_file = open("Matches//"+str(match_id)+".json", "r")
    json_data = json.loads(match_file.read())
    event_name = json_data['info']['event']['name']
    season = json_data['info']['season']
    return event_name, season


def insert_series_info(match_list):
    series_db = pd.read_csv("Series.csv", engine='python')
    match_db = pd.read_csv("Match.csv", engine='python')
    for matches in match_list:
        title, season = extract_series_info(matches)
        x = random.randint(100000, 9999999)
        if title in series_db['Title'].values:
            if season not in series_db['Season'].values:
                while x in series_db['SeriesID'].values:
                    x = + 1
                series_db.loc[len(series_db.index)] = [
                    title, season, x]
        else:
            while x in series_db['SeriesID'].values:
                x = + 1
            series_db.loc[len(series_db.index)] = [title, season,
                                                   x]
    series_db.to_csv("Series.csv", index=False)


def insert_match_info(match_list):
    series_db = pd.read_csv("series.csv", engine='python')
    match_db = pd.read_csv("Match.csv", engine='python')
    player_db = pd.read_csv("Playerdatabase.csv", engine='python')
    for matches in match_list:
        match_id, match_type, match_date, event_name, event_stage, field_umpires_1, field_umpires_2, tv_umpire, winner_team, result_description, player_of_match, season, team_type, team_1, team_2 = extract_matchinfo(
            matches)
        if int(matches) not in match_db['MatchID'].values:
            print(player_of_match)
            player_db = player_db.loc[player_db['Scrapped Name']
                                      == player_of_match]
            player_of_match = player_db['ID'].values[0]
            print(matches)
            seriesid = series_db.loc[series_db['Title'] == event_name]
            seriesid = seriesid.loc[seriesid['Season'] == season]
            match_db.loc[len(match_db.index)] = [match_id, seriesid['SeriesID'].values[0], match_type, match_date, event_name, event_stage, field_umpires_1, field_umpires_2, tv_umpire,
                                                 winner_team, result_description, player_of_match, season, team_type, team_1, team_2]
    match_db.to_csv("Match.csv", index=False)
