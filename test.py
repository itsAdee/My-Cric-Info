from flask import Flask, render_template, request, redirect, url_for
from flask import *
import mysql.connector
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
#CRATE FORM CLASS
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')


my_connection = mysql.connector.connect(
    host='localhost', user='root', password='SQLKAPASSWORD', database='sakila')

mycursor = my_connection.cursor()


@app.route('/home')
def index():
    mycursor.execute("select actor_id,first_name,last_name from actor;")
    live = mycursor.fetchall()
    return render_template('Home_page.html', live_s=live)


@app.route('/home')
def Home_page():
    return render_template('Home_page.html')


@app.route('/',methods=['GET','POST'])
def stats():
    messages=[]
    # messages["name"]="llllllllll"
    name=None
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    if request.method == 'POST':
        name = request.form["name"]

        if not name:
            flash('Title is required!')
        else:
            messages.append({'name':name})
            namer = "%" + messages[0]['name']+"%"
            mycursor.execute("select actor_id,first_name,last_name from actor where first_name LIKE %s", (namer,))
            # namer = "%" + messages[0]+"%"
            # mycursor.execute("select actor_id,first_name,last_name from actor where LIKE %s", namer)
            data = mycursor.fetchall()
            #print data
            for i in data:
              print(i)
            return render_template('Home_page.html',form=form,name=name,live_s=data)

        
    return render_template('stats.html'
    ,form=form,name=name)


@app.route('/sample')
def sample():
    return render_template('sample.html')


@app.route('/live')
def live():
    my_connection = pymysql.connect(
        host='localhost', user='root', password='aliadeel1')


if __name__ == '__main__':
    app.run(debug=True)