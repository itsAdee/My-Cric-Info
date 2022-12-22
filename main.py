from flask import *
import pymysql.connections
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/',methods=['GET','POST'])
def index():
    page='live matches'
    messages=[]
    name=None
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    if request.method == 'POST':
        name = request.form["name"]
        return render_template('home.html',form=form,page=page)
 
    return render_template('form.html',form=form,page=page)


@app.route('/home')
def Home_page():
    return render_template('nav.html')


if __name__ == '__main__':
    app.run(debug=True)


