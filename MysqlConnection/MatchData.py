import csv
import pymysql
from pathlib import Path
import datetime
import pandas

wasif_password = 'SQLKAPASSWORD'
adeel_password = 'aliadeel1'
myconnection = pymysql.connect(
    host='localhost', user='root', password=adeel_password, db='cricinfosystem2')
myconnection.autocommit(True)
mycursor = myconnection.cursor()

# Using a random match id from database
Match_id = 1298150
# finding the number of innings in the match
mycursor.execute(
    'select inning from balls where match_id = %s group by inning;', [Match_id, ])
number_of_innings = mycursor.fetchall()
# these lists will contain bowler and batter info for each innings
BatterInfo = []
BowlerInfo = []
# this will store info of each bowl
BallsInfo = []
# iterating over each innings
for innings in number_of_innings:
    # finding the number of the current innings
    current_innings = innings[0]
    mycursor.execute('select fk_batter_id, runs_scored , ballfaced from batterstatsininning where fk_match_id = %s and InningNumber = %s', [
                     Match_id, current_innings])
    Innings_batters = []
    # getting batter stats for the current innings
    batter_stats = mycursor.fetchall()
    # iterating over each batter in the current innings
    for batter in batter_stats:
        current_batter = []
        current_batter.append(batter[0])
        current_batter.append(batter[1])
        current_batter.append(batter[2])
        batter_id = batter[0]
        # getting the name of the batter from the id
        mycursor.execute(
            'select concat(first_name, " ", last_name) from player where player_id = %s', [batter_id])
        names = mycursor.fetchall()
        current_batter[0] = names[0][0]
        Innings_batters.append(current_batter)
    BatterInfo.append(Innings_batters)
    mycursor.execute('select fk_bowler_id, runs , deliveries from bowlerstatsininning where fk_match_id = %s and InningNumber = %s', [
                     Match_id, current_innings])
    ##################
    # getting bowler stats for the current innings
    # repeating the same process as above
    Innings_bowlers = []
    bowler_stats = mycursor.fetchall()
    for bowler in bowler_stats:
        current_bowler = []
        current_bowler.append(bowler[0])
        current_bowler.append(bowler[1])
        current_bowler.append(bowler[2])
        bowler_id = bowler[0]
        mycursor.execute(
            'select concat(first_name, " ", last_name) from player where player_id = %s', [bowler_id])
        names = mycursor.fetchall()
        current_bowler[0] = names[0][0]
        Innings_bowlers.append(current_bowler)
    BowlerInfo.append(Innings_bowlers)
    # for each innings, we will store the info of each ball in a list
    mycursor.execute('select OverNumber, BallNumber, sum(extra_runs + scored_runs) from balls where match_id = %s and inning = %s group by OverNumber, BallNumber', [
        Match_id, current_innings])
    ball_stats = mycursor.fetchall()
    Innings_balls = []
    for ball in ball_stats:
        current_ball = []
        current_ball.append(ball[0])
        current_ball.append(ball[1])
        current_ball.append(ball[2])
        Innings_balls.append(current_ball)
    BallsInfo.append(Innings_balls)
