import MySQLdb

connect = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'test',
    charset = 'utf8'
)

cursor = connect.cursor()

print connect
print cursor

cursor.close()
connect.close()