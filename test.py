from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import pymysql
app = Flask(__name__)

my_connection = mysql.connector.connect(
    host='localhost', user='root', password='aliadeel1', database='sakila')

mycursor = my_connection.cursor()


@app.route('/')
def index():
    mycursor.execute("select actor_id,first_name,last_name from actor;")
    live = mycursor.fetchall()
    return render_template('Home_page.html', live_s=live)


@app.route('/home')
def Home_page():
    return render_template('Home_page.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/sample')
def sample():
    return render_template('sample.html')


@app.route('/live')
def live():
    my_connection = pymysql.connect(
        host='localhost', user='root', password='aliadeel1')


if __name__ == '__main__':
    app.run(debug=True)
