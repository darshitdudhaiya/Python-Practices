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

sql = "INSERT INTO tbl1 (name, email) VALUES('Steve', 'steve@gmail.com')"
cursor.execute(sql)
connection.commit()

connection.close()

print(connection)
