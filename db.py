import psycopg2
from postindex.classes import Postindex

# connect to the db
connection = psycopg2.connect(
    host='localhost',
    database='postindex',
    user='postgres',
    password='djksa%s@w'
)

# cursor
cursor = connection.cursor()
SQL_query = "SELECT * FROM public.postindex"
cursor.execute(SQL_query)
rows = cursor.fetchall()
row=rows[207]

content=Postindex(row)
content.all_content()


# close the cursor
cursor.close()

# close connection
connection.close()
