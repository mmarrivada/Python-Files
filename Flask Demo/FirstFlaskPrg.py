from flask import Flask,request,render_template

app = Flask(__name__)               #main entire website..helpful to determine root path

users = [ ]
users.append({"name": "rajesh", "type": "admin", 'password': 'rajesh'})
users.append({"name": "madhavi", "type": "user", 'password': 'madhavi'})
users.append({"name": "priyanka", "type": "user", 'password': 'priyanka'})



@app.route('/')                     # What ever webpage you wana connect
def index():
    return 'This is the home page '

# @app.route('/profile/<username>')       # var name should be in <>
# def profile(username):
#     return '<h2>Hey %s <h2>' % username       # not recommended to write html code in return statement use htmltemplates

@app.route('/post/<int:post_id>')           # var of integer <int:var_name>
def post_id(post_id):
    return '<h3>Post id is: %s <h3>' %post_id

@app.route('/method/' , methods = ['GET','POST'])       #how to call http methods
def method():
    if request.method == 'GET':
        return "You are in method %s" % request.method          # mostly will use get
    else:
       return "You are in method %s" % request.method           # in froms we will use post

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/users')
def user_list():
    return render_template('users1.html', users=users)

@app.route('/dict')
def dict():
    parent_dict = [{'A': 'val1', 'B': 'val2'}, {'C': 'val3', 'D': 'val4'}]
    return render_template('usertable.html',parent_dict = parent_dict )

if __name__ == "__main__":          # only run app  this file call directly
    app.run(debug = True)           # start the web server

