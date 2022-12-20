import json
import pandas as pd
import random
from pathlib import Path
import os


def extract_teams():
    current = Path.cwd()
    matches_csv = pd.read_csv("Teams.csv")
    matches_path = current / "Matches"
    print(matches_path)
    x = 1
    for file in os.listdir(matches_path):
        if file.endswith(".json"):
            id = file.split(".")[0]
            myfile = open("Matches//"+str(id)+".json", "r")
            json_data = json.loads(myfile.read())
            teams = json_data['info']['teams']
            teamtype = json_data['info']['team_type']

            for team in teams:
                if team not in matches_csv['TeamName'].values:
                    if teamtype == "international":
                        matches_csv = matches_csv.append(
                            {'TeamName': team, 'Team_id': x, 'isInternational': "1"}, ignore_index=True)
                        x += 1
                    else:
                        matches_csv = matches_csv.append(
                            {'TeamName': team, 'Team_id': x, 'isInternational': "0"}, ignore_index=True)
                        x += 1
                matches_csv.to_csv("Teams.csv", index=False)


extract_teams()
