import csv
import pymysql
from pathlib import Path
import datetime
import pandas

wasif_password = 'SQLKAPASSWORD'
adeel_password = 'aliadeel1'
myconnection = pymysql.connect(
    host='localhost', user='root', password=adeel_password)
myconnection.autocommit(True)
mycursor = myconnection.cursor()
mycursor.execute('USE cricinfosystem2')
mycursor.execute("select count(*)  as wickets , BowlerId from wicketstatsinnings where BowlerId in ( select player_id  from player where Country = 'Pakistan' )and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20') group by BowlerId")
myresult = mycursor.fetchall()
max_wickets = myresult[0][0]
id = myresult[0][1]
for x in myresult:
    if x[0] > max_wickets:
        max_wickets = x[0]
        id = x[1]
print(id)
