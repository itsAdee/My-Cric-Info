import csv
import pymysql
from pathlib import Path
import datetime
import pandas

myconnection = pymysql.connect(
    host='localhost', user='root', password='aliadeel1')
myconnection.autocommit(True)
mycursor = myconnection.cursor()
cwd = Path.cwd().parent


def InsertPlayers():
    file = open('Playerdatabase.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    for rows in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        id = rows[0]
        first_name = rows[1]
        last_name = rows[2]
        country = rows[4]
        dob = rows[5].split(' ')[0]
        print(dob)
        batting_style = rows[6]
        bowling_style = rows[7]
        mycursor.execute('delete from player')
        q = 'INSERT INTO player ( player_id  ,First_name , Last_Name , Country ,DOB ,Batting_style ,Bowling_style ,fk_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (id, first_name, last_name, country,
                  dob, batting_style, bowling_style, id)
        mycursor.execute(q, values)


def InsertSeries():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//series.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from series')
    for rows in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        title = str(rows[0])
        season = str(rows[1])
        SeriesID = str(rows[2])
        istournament = str(1 if 'Cup' in title or 'cup' in title else 0)
        q = 'Insert into series( series_id,isTournament,Title,season) VALUES (%s,%s,%s,%s)'
        values = (SeriesID, istournament, title, season)
        mycursor.execute(q, values)


def InsertTeams():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//Teams.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from team')
    for rows in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        TeamName = str(rows[0])
        team_id = str(rows[1])
        is_international = str(rows[2])
        q = 'Insert into team(team_id,team_name,isInternational) VALUES (%s,%s,%s)'
        values = (team_id, TeamName, is_international)
        mycursor.execute(q, values)


def InsertMatches():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//Match.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from matchfixture')

    for rows in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        match_id = rows[0]
        series_id = rows[1]
        match_type = rows[2]
        match_date = rows[3]
        event_name = rows[4]
        event_stage = rows[5]
        field_umpire_1 = rows[6]
        field_umpire_2 = rows[7]
        Tv_Umpire = rows[8]
        winner_team = rows[9]
        result_description = rows[10]
        player_of_match = rows[11]
        team_1 = rows[13]
        teams_2 = rows[14]
        q = 'Insert into matchfixture( Match_id,series_id,match_type,MatchDate,event_name,event_stage,field_umpire_1,field_umpire_2,TV_empire,fk_team_1_id,fk_team_2_id,Matchwinner,Matchwinner_desc,player_of_match) VALUES (%s,%s,%s,%s)'
        values = (match_id, series_id, match_type, match_date, event_name, event_stage, field_umpire_1,
                  field_umpire_2, Tv_Umpire, winner_team, result_description, player_of_match, team_1, teams_2)
        mycursor.execute(q, values)


def Insertballs():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//BallDatabase.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from balls')
    for rows in file:
        Match_id = rows[0]
        Inning = rows[1]
        overNumber = rows[2]
        BallNumber = rows[3]
        extra_runs = rows[4]
        scored_runs = rows[5]
        bowler = rows[6]
        batter = rows[7]
        q = 'Insert into balls(Match_id,inning,OverNumber,BallNumber,extra_runs,scored_runs,bowler,batter)'
        values = (Match_id, Inning, overNumber, BallNumber,
                  extra_runs, scored_runs, bowler, batter)
        mycursor.execute(q, values)


def InsertBatter():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//BatterInfo.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from batterstatsininning')
    for rows in file:
        Match_id = rows[0]
        Inning = rows[1]
        batter = rows[2]
        runs = rows[3]
        balls = rows[4]
        q = 'Insert into batterstatsininning(fk_Match_id,InningNumber,fk_batter_id,runs_scored,balls_faced)'
        values = (Match_id, Inning, batter, runs, balls)
        mycursor.execute(q, values)


def InsertBowler():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//BowlerInfo.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from bowlerstatsininning')
    for rows in file:
        bowler = rows[0]
        runs = rows[1]
        deliveries = rows[2]
        match_id = rows[3]
        innings = rows[4]
        q = 'Insert into batterstatsininning(fk_Match_id,InningNumber,fk_bowler_id,runs,deliveries)'
        values = (bowler, runs, deliveries, match_id, innings)
        mycursor.execute(q, values)


def InsertWicketsInfo():
    cwd = Path.cwd().parent
    file = open(cwd / 'Filteration//wicketinfo.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    mycursor.execute('delete from wicketstatsinnings')
    for rows in file:
        batter = rows[0]
        bowler = rows[1]
        Inning = rows[3]
        match_id = rows[7]
        over = rows[8]
        Ball = rows[9]
        Description = rows[10]
        q = 'Insert into wicketstatsinnings(BatterId,BowlerId,InningNumber,fk_Match_id,OverNumber,BallNumber,WicketDescription)'
        values = (batter, bowler, Inning, match_id, over, Ball, Description)
        mycursor.execute(q, values)
