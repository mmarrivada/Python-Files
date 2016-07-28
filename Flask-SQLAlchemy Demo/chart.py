from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost/FlaskMovie'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

db = SQLAlchemy(app)

class Chart(db.Model):

    # __tablename__ = 'chart'
    task = db.Column(db.Integer, primary_key = True)
    hoursperday = db.Column(db.String(80))

    def __init__(self,task,hoursperday):
        self.task = task
        self.hoursperday = hoursperday


@app.route('/')
def home():

    return render_template('add_details.html')


@app.route('/post_details',methods = ['POST'])
def post_details():
    chart = Chart( request.form['task'] , request.form['hoursperday'])
    db.session.add(chart)
    db.session.commit()
    return redirect(url_for('add_details.html'))



if __name__ == "__main__":
    app.debug = True
    app.run()


