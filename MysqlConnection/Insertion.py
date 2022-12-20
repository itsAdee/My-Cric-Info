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
    file = open(cwd / 'Series.csv', 'r')
    mycursor.execute('USE cricinfosystem2')
    csv_data = csv.reader(file)
    skipHeader = True
    for rows in csv_data:
        if skipHeader:
            skipHeader = False
            continue
        title = rows[0]
        season = rows[1]
        SeriesID = rows[2]
        istournament = 1 if 'Cup' in title or 'cup' in title else 0
        q = 'Insert into player( series_id,isTournament,Title,season,player_of_series)'
        values = (id, first_name, last_name, country,
                  dob, batting_style, bowling_style, id)
        mycursor.execute(q, values)
