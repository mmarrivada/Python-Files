from flask import *
# from db1 import *
from db import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('login.pt')

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         uname = request.form['uname']
#         password = request.form['password']
#         user = get_user(uname)
#         if user and user.get('password', '') == password:
#             tasks = get_user_tasks(user)
#             return render_template('tasks.html', tasks=tasks)
#
#     return render_template('task_form.html')

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == 'POST':
       uname = request.form['uname']
       password = request.form['password']
       user = get_details()
       if user and user.get('password', '') == password:
           print(user.id,user.task)
    return render_template('task_form.html')



@app.route("/addtask",methods = ['POST'])
def addtask():
    if request.method == 'POST':
       id   = request.form['id']
       task = request.form['task']
    return updatetasks(id,task)
    #return "It worked"








@app.route('/users')
def users_list():
    return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)