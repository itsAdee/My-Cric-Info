from ExtractBallInformation import extractballinfo
import pandas as pd
import json

overs, ball_number, extra, hallal_runs, bowler, batter = extractballinfo(
    1327281, 0)
dataframe = pd.DataFrame({'overs': overs, 'ball_number': ball_number, 'extra': extra,
                         'hallal_runs': hallal_runs, 'bowler': bowler, 'batter': batter})


def extract_batterInfo(dataframe):
    df2 = dataframe.groupby(['batter'])['hallal_runs'].sum()
    df2 = df2.reset_index()
    df3 = dataframe.groupby(['batter']).count()
    df3 = df3.reset_index()
    batter = []
    runs = []
    balls = []
    for i in range(len(df2)):
        batter.append(df2['batter'][i])
        runs.append(df2['hallal_runs'][i])
        balls.append(df3['hallal_runs'][i])
    batter = pd.DataFrame({'batter': batter, 'runs': runs, 'balls': balls})
    batter.to_csv('BatterInfo.csv', index=False)


def extract_bowlerInfo(dataframe):
    df2 = dataframe.groupby(['bowler'])['hallal_runs'].sum().reset_index()
    df3 = dataframe.groupby(['bowler']).count().reset_index()
    bowler = []
    runs = []
    deliveries = []
    for i in range(len(df2)):
        bowler.append(df2['bowler'][i])
        runs.append(df2['hallal_runs'][i])
        deliveries.append(df3['hallal_runs'][i])
    bowler = pd.DataFrame(
        {'bowler': bowler, 'runs': runs, 'deliveries': deliveries})
    bowler.to_csv('BowlerInfo.csv', index=False)


extract_bowlerInfo(dataframe)
