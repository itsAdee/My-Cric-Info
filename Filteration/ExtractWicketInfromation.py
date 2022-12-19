import pandas as pd
import json


def extractwicketinfo(match_id, inning_number):
    ball_file = open("Matches//"+str(match_id)+".json", "r")
    ball_file = json.loads(ball_file.read())
    over = []
    ball_number = []
    bowler = []
    batter = []
    description = []
    for i in ball_file['innings'][inning_number]['overs']:
        x = 1
        for j in i['deliveries']:
            try:

                description.append(j['wickets'][0]['kind'])
                over.append(i['over'])
                ball_number.append(x)
                bowler.append(j['bowler'])
                batter.append(j['wickets'][0]['player_out'])

                try:
                    caught_by = j['wickets'][0]['fielders'][0]
                    if description == 'run out':
                        description.append("Caught by "+caught_by)
                    else:
                        description.append("Caught by "+caught_by)
                except:
                    print("Caught by not found")
                    pass
            except:
                print("Wicket not found")
                x += 1
                continue
            x += 1
    return over, ball_number, bowler, batter, description


def InsertBallInfo(matchlist):
    for match_id in matchlist:
        match_db = pd.read_csv("Match.csv")
        player_db = pd.read_csv("Playerdatabase.csv")
        wicket_db = pd.read_csv("wicketinfo.csv")
        if int(match_id) in match_db['MatchID'].values:
            for y in range(2):
                over, ball_number, bowler, batter, description = extractwicketinfo(
                    match_id=match_id, inning_number=y)
                for i in range(len(over)):
                    batter_id = player_db.loc[player_db['Scrapped Name']
                                              == batter[i]]
                    batter_id = batter_id['ID'].values[0]
                    bowler_id = player_db.loc[player_db['Scrapped Name']
                                              == bowler[i]]
                    bowler_id = bowler_id['ID'].values[0]
                    wicket_db = wicket_db.append({'MatchId': match_id, 'Inning': y, 'Over': over[i], 'BallNumber': ball_number[
                                                 i], 'Bowler': bowler_id, 'Batter': batter_id, 'Description': description[i]}, ignore_index=True)
    wicket_db.to_csv("wicketinfo.csv", index=False)


InsertBallInfo([1327281])
