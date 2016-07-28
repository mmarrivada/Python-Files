from flask import *
app = Flask(__name__)

users = []
users.append({"name": "Jhon", "type": "admin", 'password': 'Jhon'})
users.append({"name": "Nana", "type": "user", 'password': 'Nana'})
users.append({"name": "Donny", "type": "user", 'password': 'Donny'})

# @app.route("/")
# def home():
#     return render_template('login.pt')
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#         password = request.form['password']
#         for user in users:
#             if user['name'] == uname and user['password'] == password:
#                 return "Welcome {}".format(uname)
#
#     if request.method == 'POST':
#         uname = request.form['uname']
#         return "Invalid user."
#     return render_template('login.pt')
# @app.route('/users')
# # def users_list():
# #
# #     return render_template('user.pt', users)

@app.route('/list')
def users_list():

        return render_template('users1.html',users = users)


if __name__ == "__main__":
    app.run(debug=True)
