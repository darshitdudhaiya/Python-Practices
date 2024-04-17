from mysql.connector import connect


host = "localhost"
dbname = "db1"
username = "root"
password = ""

connection = connect(
    host=host,
    username=username,
    password=password,
    database=dbname,
)

cursor = connection.cursor()

sql = "SELECT * FROM tbl1"
cursor.execute(sql)
records = cursor.fetchall()

print(records)

connection.close()

print(connection)
