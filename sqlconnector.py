import mysql.connector

my_connection = mysql.connector.connect(
    host='localhost', user='root', password='aliadeel1', database='sakila')

mycursor = my_connection.cursor()

mycursor.execute("select actor_id,first_name,last_name from actor;")

for x in mycursor.fetchall():
    print(x)
