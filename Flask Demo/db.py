import psycopg2

conn = psycopg2.connect(database = 'FlaskMovie',user = 'postgres',password = 'admin',host = '127.0.0.1',port = '5432')

print("Connected to database sampledb")

cur = conn.cursor()

sql = ("select hrs_day from chart")
def get_details()