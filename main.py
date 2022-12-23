from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


class MyForm(FlaskForm):
    team_name = StringField('team_name', validators=[DataRequired()])
    season = StringField('season', validators=[DataRequired()])
    match_type = StringField('match_type', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/index')
def index():

    return render_template('index.html')


@app.route('/home')
def Home_page():
    return render_template('Home_page.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/sample')
def sample():
    return render_template('sample.html')


@app.route('/player')
def player():
    return render_template('player.html')


@app.route('/teams', methods=['GET', 'POST'])
def teams():
    page = 'live matches'
    messages = []
    team_name = None
    form = MyForm()
    if form.validate_on_submit():
        team_name = form.team_name.data
        form.team_name.data = ''
        
    if form.validate_on_submit():
        team_name = form.season.data
        form.season.data = ''
        
    if form.validate_on_submit():
        team_name = form.match_type.data
        form.match_type.data = ''
        
    if request.method == 'POST':
        team_name = request.form["team_name"]
        team_name = request.form["season"]
        team_name = request.form["match_type"]
        return render_template('Home_page.html', form=form, page=page, name=team_name)

    return render_template('teams.html', form=form, name=team_name)


if __name__ == '__main__':
    app.run(debug=True)
