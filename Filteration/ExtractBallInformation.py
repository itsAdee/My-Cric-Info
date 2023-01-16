import pandas as pd
import json


def extract_batterInfo(dataframe, inning_number, match_id):
    batter = pd.read_csv("BatterInfo.csv")
    if (match_id not in batter['MatchID'].values):
        df2 = dataframe.groupby(['Batter'])['HallalRuns'].sum()
        df2 = df2.reset_index()
        df3 = dataframe.groupby(['Batter']).count()
        df3 = df3.reset_index()

        for i in range(len(df2)):
            batter = batter.append({'Batter': df2['Batter'][i], 'Runs': df2['HallalRuns'][i],
                                    'Balls': df3['HallalRuns'][i], 'MatchID': match_id, 'Inning': inning_number}, ignore_index=True)
        batter.to_csv('BatterInfo.csv', index=False)


def extract_bowlerInfo(dataframe, inning_number, match_id):
    bowler = pd.read_csv("BowlerInfo.csv")
    if (match_id not in bowler['MatchID'].values):
        df2 = dataframe.groupby(['Bowler'])['HallalRuns'].sum().reset_index()
        df3 = dataframe.groupby(['Bowler']).count().reset_index()

        for i in range(len(df2)):
            bowler = bowler.append({'Bowler': df2['Bowler'][i], 'Runs': df2['HallalRuns'][i],
                                    'Deliveries': df3['HallalRuns'][i], 'MatchID': match_id, 'Inning': inning_number}, ignore_index=True)
        bowler.to_csv('BowlerInfo.csv', index=False)


def extractballinfo(match_id, inning_number):
    ball_file = open("Matches//"+str(match_id)+".json", "r")
    ball_file = json.loads(ball_file.read())
    overs = []
    ball_number = []
    extra = []
    hallal_runs = []
    bowler = []
    batter = []
    for i in ball_file['innings'][inning_number]['overs']:
        x = 1
        for j in i['deliveries']:
            overs.append(i['over'])
            hallal_runs.append(j['runs']['batter'])
            extra.append(j['runs']['extras'])
            ball_number.append(x)
            bowler.append(j['bowler'])
            batter.append(j['batter'])
            x += 1
    return overs, ball_number, extra, hallal_runs, bowler, batter


def InsertBallInfo(matchlist):
    for match_id in matchlist:
        match_db = pd.read_csv("Match.csv")
        player_db = pd.read_csv("Playerdatabase.csv")
        ball = pd.read_csv("BallDatabase.csv")
        if int(match_id) in match_db['MatchID'].values and int(match_id) not in ball['MatchId'].values:
            print(match_id)
            format = match_db.loc[match_db['MatchID'] == int(match_id)]
            format = format['MatchType'].values[0]
            if format == 'ODI' or format == 'T20':
                my_range = 2

            elif format == 'Test':
                my_range = 4

            for y in range(4):
                ball = pd.read_csv("BallDatabase.csv")
                db = ball.loc[ball['MatchId'] == match_id]
                overs = []
                ball_number = []
                extra = []
                hallal_runs = []
                bowler = []
                batter = []
                try:
                    if y not in db['Inning'].values:
                        ball_file = open(
                            "Matches//"+str(match_id)+".json", "r")
                        ball_file = json.loads(ball_file.read())
                        for i in ball_file['innings'][y]['overs']:
                            x = 1
                            for j in i['deliveries']:
                                print(j['batter'])
                                print(j['bowler'])
                                batter_id = player_db.loc[player_db['Scrapped Name']
                                                          == j['batter']]
                                batter_id = batter_id['ID'].values[0]
                                bowler_id = player_db.loc[player_db['Scrapped Name']
                                                          == j['bowler']]
                                bowler_id = bowler_id['ID'].values[0]
                                ball = ball.append({'MatchId': match_id, 'Inning': y, 'Overs': i['over'], 'BallNumber': x, 'Extra': j['runs'][
                                    'extras'], 'HallalRuns': j['runs']['batter'], 'Bowler': bowler_id, 'Batter': batter_id}, ignore_index=True)
                                overs.append(i['over'])
                                hallal_runs.append(j['runs']['batter'])
                                extra.append(j['runs']['extras'])
                                ball_number.append(x)
                                bowler.append(bowler_id)
                                batter.append(batter_id)
                                x += 1
                        Inning_db = pd.DataFrame({'MatchId': match_id, 'Inning': y, 'Overs': overs, 'BallNumber': ball_number,
                                                  'Extra': extra, 'HallalRuns': hallal_runs, 'Bowler': bowler, 'Batter': batter})
                        extract_batterInfo(Inning_db, y, match_id)
                        extract_bowlerInfo(Inning_db, y, match_id)
                    ball.to_csv("BallDatabase.csv", index=False)
                except:
                    print("Continuing for "+str(match_id))
