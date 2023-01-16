from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import mysql.connector
from pathlib import Path

my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='cricinfosystem2')

mycursor = my_connection.cursor()



app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


class MyForm(FlaskForm):
    team_name_1 = StringField('First Team Name', validators=[DataRequired()])
    season = StringField('season', validators=[DataRequired()])
    team_name_2 = StringField('Second Team Name', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/about')
def about():
    return render_template('Home_page.html')


@app.route('/team_stats')
def team_stats():
    mycursor.execute("SELECT team_name FROM cricinfosystem2.team;")
    myresult = mycursor.fetchall()
    teamStats=[]
    for x in myresult:
        x=list(x)
        mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'T20'",(x[0],x[0],x[0]))
        losses=mycursor.fetchall()
        x.append(losses[0][0])
        mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'T20'",(x[0],x[0],))
        draws=mycursor.fetchall()
        x.append(draws[0][0])
        mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'T20'",(x[0],x[0],x[0]))
        wins=mycursor.fetchall()
        x.append(wins[0][0])
        mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by BowlerId",(x[0],))
        myresult = mycursor.fetchall()
        max_wickets = myresult[0][0]
        id = myresult[0][1]
        for k in myresult:
            if k[0] > max_wickets:
                max_wickets = k[0]
                id = k[1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        x.append(name)
        x.append(max_wickets)
        
        mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by fk_batter_id) as sub ",(x[0],))
        myresult = mycursor.fetchall()
        max_runs = myresult[0][0]
        id = myresult[0][1]
        mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
        name = mycursor.fetchall()
        name = name[0][0] + " " + name[0][1]
        x.append(name)
        x.append(max_runs)


        #do the same task for ODI and Test
        mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'ODI'",(x[0],x[0],x[0]))
        losses=mycursor.fetchall()
        x.append(losses[0][0])
        mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'ODI'",(x[0],x[0],))
        draws=mycursor.fetchall()
        x.append(draws[0][0])
        mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'ODI'",(x[0],x[0],x[0]))
        wins=mycursor.fetchall()
        x.append(wins[0][0])
        mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'ODI') group by BowlerId",(x[0],))
        myresult = mycursor.fetchall()
        if myresult:
            max_wickets = myresult[0][0]
            id = myresult[0][1]
            for k in myresult:
                if k[0] > max_wickets:
                    max_wickets = k[0]
                    id = k[1]
            mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
            name = mycursor.fetchall()
            name = name[0][0] + " " + name[0][1]
            x.append(name)
            x.append(max_wickets)
        else:
            x.append("No data")
            x.append("No data")

        mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'ODI') group by fk_batter_id) as sub ",(x[0],))
        
        myresult = mycursor.fetchall()
        if myresult[0][0]:
            max_runs = myresult[0][0]
            id = myresult[0][1]
            mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
            name = mycursor.fetchall()
            name = name[0][0] + " " + name[0][1]
            
            x.append(name)
            x.append(max_runs)
        else:
            x.append("No data")
            x.append("No data")


        mycursor.execute("select count(*) as losses from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner not  in ( select team_id from team where team_name = %s) and Matchwinner != 0 and match_type = 'Test'",(x[0],x[0],x[0]))
        losses=mycursor.fetchall()
        x.append(losses[0][0])
        mycursor.execute("select count(*) as draws from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner = 0 and match_type = 'Test'",(x[0],x[0],))
        draws=mycursor.fetchall()
        x.append(draws[0][0])
        mycursor.execute("select count(*) as wins from matchfixture where (fk_team_1_id in ( select team_id from team  where  team_name = %s) or fk_team_2_id in (select team_id from team where team_name = %s)) and Matchwinner in ( select team_id from team where team_name = %s) and match_type = 'Test'",(x[0],x[0],x[0]))
        wins=mycursor.fetchall()
        x.append(wins[0][0])
        mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = %s )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'Test') group by BowlerId",(x[0],))
        myresult = mycursor.fetchall()

        if myresult:
            max_wickets = myresult[0][0]
            id = myresult[0][1]
            for k in myresult:
                if k[0] > max_wickets:
                    max_wickets = k[0]
                    id = k[1]
            mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
            name = mycursor.fetchall()
            name = name[0][0] + " " + name[0][1]
            x.append(name)
            x.append(max_wickets)
        else:
            x.append("No data")
            x.append("No data")

        mycursor.execute(" select max(total_runs) , fk_batter_id from (select (sum(runs_scored)) as total_runs , fk_batter_id from batterstatsininning where fk_batter_id in ( select player_id  from player where Country =%s) and fk_Match_Id in (select Match_id from matchfixture where match_type = 'Test') group by fk_batter_id) as sub ",(x[0],))

        myresult = mycursor.fetchall()
        if myresult[0][0]:
            max_runs = myresult[0][0]
            id = myresult[0][1]
            mycursor.execute("select First_name,Last_Name from player where player_id = %s and Country=%s",(id,x[0],))
            name = mycursor.fetchall()
            name = name[0][0] + " " + name[0][1]
            
            x.append(name)
            x.append(max_runs)
        else:
            x.append("No data")
            x.append("No data")

        teamStats.append(x)
    return render_template('team_stats.html',teamStats=teamStats)


@app.route('/sample')
def sample():
    return render_template('sample.html')


@app.route('/player')
def player():
    mycursor.execute("SELECT * FROM cricinfosystem2.player;")
    players=mycursor.fetchall()
    n=0
    playersData=[]
    for i in players:
        #covert i to list
        i=list(i)
        #append player id to list
        mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_bowler_id;",(i[0],))
        economy_rate=mycursor.fetchall()
        if len(economy_rate)==0:
            economy_rate=[(None,)]
            #append in i array
            i.append(economy_rate[0][0])
        else:
            i.append(economy_rate[0][0])
        mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_bowler_id;",(i[0],))
        economy_rate=mycursor.fetchall()
        if len(economy_rate)==0:
            economy_rate=[(None,)]
            #append in i array
            i.append(economy_rate[0][0])
        else:
            i.append(economy_rate[0][0])
        mycursor.execute("select sum(runs)/(sum(deliveries) /6) as Economy_Rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_bowler_id;",(i[0],))
        economy_rate=mycursor.fetchall()
        if len(economy_rate)==0:
            economy_rate=[(None,)]
            #append in i array
            i.append(economy_rate[0][0])
        else:
            i.append(economy_rate[0][0])
        
        mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
        avg=mycursor.fetchall()
        if len(avg)==0:
            avg=[(None,)]
            i.append(avg[0][0])
        else:
            i.append(avg[0][0])

        mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
        avg=mycursor.fetchall()
        if len(avg)==0:
            avg=[(None,)]
            i.append(avg[0][0])
        else:
            i.append(avg[0][0])
        
        mycursor.execute("select sum(runs_scored)/count(fk_Match_Id) as Avg from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
        avg=mycursor.fetchall()
        if len(avg)==0:
            avg=[(None,)]
            i.append(avg[0][0])
        else:
            i.append(avg[0][0])
        

        mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
        total_matches=mycursor.fetchall()
        if len(total_matches)==0:
            total_matches=[(None,)]
            i.append(total_matches[0][0])
        else:
            i.append(total_matches[0][0])

        mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
        total_matches=mycursor.fetchall()
        if len(total_matches)==0:
            total_matches=[(None,)]
            i.append(total_matches[0][0])
        else:
            i.append(total_matches[0][0])

        mycursor.execute("select count(fk_Match_Id) as total_Matches from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
        total_matches=mycursor.fetchall()
        if len(total_matches)==0:
            total_matches=[(None,)]
            i.append(total_matches[0][0])
        else:
            i.append(total_matches[0][0])

        
        mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])

        mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])

        mycursor.execute("select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by BowlerId , fk_match_id having count(*) >= 3) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by BowlerId , fk_match_id having count(*) >= 5) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by BowlerId , fk_match_id having count(*) >= 5) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(*) as '3w' from (select count(*) as '3w' from wicketstatsinnings where BowlerId in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by BowlerId , fk_match_id having count(*) >= 5) as anothertable",(i[0],))
        wickets=mycursor.fetchall()
        if len(wickets)==0:
            wickets=[(None,)]
            i.append(wickets[0][0])
        else:
            i.append(wickets[0][0])

        mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) and runs_scored > 50 group by fk_batter_id",(i[0],))
        fifties=mycursor.fetchall()
        if len(fifties)==0:
            fifties=[(None,)]
            i.append(fifties[0][0])
        else:
            i.append(fifties[0][0])
        
        mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) and runs_scored > 50 group by fk_batter_id",(i[0],))  
        fifties=mycursor.fetchall()
        if len(fifties)==0:
            fifties=[(None,)]
            i.append(fifties[0][0])
        else:
            i.append(fifties[0][0])

        mycursor.execute("select count(fk_Match_Id) as '50s' from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) and runs_scored > 50 group by fk_batter_id",(i[0],))
        fifties=mycursor.fetchall()
        if len(fifties)==0:
            fifties=[(None,)]
            i.append(fifties[0][0])
        else:
            i.append(fifties[0][0])

        mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_batter_id",(i[0],))
        highest_score=mycursor.fetchall()
        if len(highest_score)==0:
            highest_score=[(None,)]
            i.append(highest_score[0][0])
        else:
            i.append(highest_score[0][0])

        mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_batter_id",(i[0],))
        highest_score=mycursor.fetchall()
        if len(highest_score)==0:
            highest_score=[(None,)]
            i.append(highest_score[0][0])
        else:
            i.append(highest_score[0][0])

        mycursor.execute("select max(runs_scored) from batterstatsininning where fk_batter_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_batter_id",(i[0],))
        highest_score=mycursor.fetchall()
        if len(highest_score)==0:
            highest_score=[(None,)]
            i.append(highest_score[0][0])
        else:
            i.append(highest_score[0][0])

        mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' ) group by fk_bowler_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])

        mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'ODI' ) group by fk_bowler_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])

        mycursor.execute("select sum(runs)/sum(deliveries) * 100 as strike_rate from bowlerstatsininning where fk_bowler_id in ( select player_id from player where player_id=%s ) and fk_match_id in ( select Match_id from matchfixture where match_type = 'Test' ) group by fk_bowler_id",(i[0],))
        strike_rate=mycursor.fetchall()
        if len(strike_rate)==0:
            strike_rate=[(None,)]
            i.append(strike_rate[0][0])
        else:
            i.append(strike_rate[0][0])


        
        playersData.append(i)
    return render_template('player.html',players=playersData)


@app.route('/',)
def home():
    return render_template('opening_page.html')


@app.route('/teams', methods=['GET', 'POST'])
def teams():
    team_name_1 = None
    season = None
    team_name_2 = None
    form = MyForm()
    if form.validate_on_submit():
        team_name_1 = form.team_name_1.data
        form.team_name_1.data = ''
        
    if form.validate_on_submit():
        season = form.season.data
        form.season.data = ''
        
    if form.validate_on_submit():
        team_name_2 = form.team_name_2.data
        form.team_name_2.data = ''
        
    if request.method == 'POST':
        team_name_1 = request.form["team_name_1"]
        season = request.form["season"]
        team_name_2 = request.form["team_name_2"]
        matchData=[]
        mycursor.execute("Select event_name,MatchDate,  match_id,fk_team_1_id,fk_team_2_id, Matchwinner_desc from matchfixture join series using(series_id) where fk_team_1_id in (select team_id from team where team_name = %s or team_name like CONCAT('%', %s, '%')) and fk_team_2_id in (select team_id from team where team_name = %s or team_name like CONCAT('%', %s, '%'))",(team_name_1,team_name_2,team_name_1,team_name_2))
        available_matches=mycursor.fetchall()
        for i in available_matches:
            if i[0]=="England tour of Pakistan":
                continue
            my_match = []
            for j in i:
                my_match.append(j)
                



            mycursor.execute("select sum(extra_runs) + sum(scored_runs) as Totalscore from balls where match_id=%s  group by Match_id,inning;",(my_match[2],))
            total_score=mycursor.fetchall()


            mycursor.execute("select count(*) as wickets from wicketstatsinnings where fk_match_id=%s  group by fk_Match_id,InningNumber", (my_match[2],))
            wickets=mycursor.fetchall()

            for t in zip(total_score,wickets):
                    my_match.append(t)
            matchData.append(my_match)
        for u in matchData:
            mycursor.execute("select team_name from team where team_id=%s;",(u[3],))
            u[3]=mycursor.fetchall()[0][0]
            mycursor.execute("select team_name from team where team_id=%s;",(u[4],))
            u[4]=mycursor.fetchall()[0][0]

        print(matchData) 
        return render_template('available_matches.html', form=form, name1=team_name_1,season=season,name2=team_name_2,matchData=matchData)

    return render_template('teams.html', form=form, name=team_name_1,season=season,match_type=team_name_2)



@app.route('/index', methods=['GET', 'POST'])
def index():
    # finding the number of innings in the match
    Match_id  = request.args.get('Match_id', None)
    team_1=request.args.get('team_1', None)
    team_2=request.args.get('team_2', None)
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
            print(batter_id)
            mycursor.execute(
                'select BowlerId,OverNumber,BallNumber,WicketDescription from wicketstatsinnings where BatterId = %s and fk_match_id=%s', (batter_id,Match_id))
            wicket_infor = mycursor.fetchall()
            if(wicket_infor):
                current_batter.append(wicket_infor[0][0])
                current_batter.append(wicket_infor[0][1])
                current_batter.append(wicket_infor[0][2])
                current_batter.append(wicket_infor[0][3])
                baller_id=current_batter[3]
                mycursor.execute(
                    'select concat(first_name, " ", last_name) from player where player_id = %s', [baller_id])
                names = mycursor.fetchall()
                current_batter[3] = names[0][0]
            else:
                current_batter.append(None)
                current_batter.append(None)
                current_batter.append(None)
                current_batter.append(None)

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
            mycursor.execute(
                'select BatterId,OverNumber,BallNumber,WicketDescription from wicketstatsinnings where BowlerId = %s and fk_match_id=%s', (bowler_id,Match_id))
            wicket_infor = mycursor.fetchall()
            if(wicket_infor):
                current_bowler.append(wicket_infor[0][0])
                current_bowler.append(wicket_infor[0][1])
                current_bowler.append(wicket_infor[0][2])
                current_bowler.append(wicket_infor[0][3])
                batter_id=current_bowler[3]
                mycursor.execute(
                    'select concat(first_name, " ", last_name) from player where player_id = %s', [batter_id])
                names = mycursor.fetchall()
                current_bowler[3] = names[0][0]
            else:
                current_bowler.append(None)
                current_bowler.append(None)
                current_bowler.append(None)
                current_bowler.append(None)
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


    return render_template('match_stats.html',team_1=team_1,team_2=team_2,BatterInfo=BatterInfo,BowlerInfo=BowlerInfo,BallsInfo=BallsInfo)



if __name__ == '__main__':
    app.run(debug=True)
