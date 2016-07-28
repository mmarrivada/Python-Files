import psycopg2

conn = psycopg2.connect(database = 'FlaskMovie',user = 'postgres',password = 'admin',host = '127.0.0.1',port = '5432')
print("Connected successfully!!")
cursor = conn.cursor()

def get_details():
    sql = "select * from chart "
    cursor.execute(sql)
    activites = [['Activities', 'hours spent']]
    user_activites = cursor.fetchall()
    for user_record in user_activites:

        activites.append([ user_record[0], user_record[1]])
    return activites