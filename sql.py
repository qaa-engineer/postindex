import psycopg2

# connect to the db
connection = psycopg2.connect(
    host='localhost',
    database='postindex',
    user='postgres',
    password='djksa%s@w'
)
# cursor
cursor = connection.cursor()
SQL_query = "SELECT postindex, opsname, region, area, city FROM public.postindex"
cursor.execute(SQL_query)
rows = cursor.fetchall()

print(rows[47000])

#close the cursor
cursor.close()

# close connection
connection.close()
