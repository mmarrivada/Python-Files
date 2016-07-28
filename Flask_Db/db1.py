import psycopg2


conn = psycopg2.connect("dbname='FlaskMovie' user='postgres' host='localhost' port='5432' password='admin'")
print("Connected successfully!!")
cursor = conn.cursor()

def get_user(uname):
    sql = "select * from users where name='{}'".format(uname)
    cursor.execute(sql)
    user = None
    user_record = cursor.fetchone()
    if user_record:

        user = { 'id' : user_record[0],
                 'uname' : user_record[1],
                 'password' : user_record[2]
                 }
    return user

def get_user_tasks(user):
    sql = "select * from tasks where uid={}".format(user.get('id'))
    cursor.execute(sql)
    tasks = []
    user_tasks = cursor.fetchall()
    for task in user_tasks:
        tasks.append({
                    'id': task[0],
                    'task': task[2],
                    'status': task[3]
        })
    return tasks
