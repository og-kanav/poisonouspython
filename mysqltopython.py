import mysql.connector as i
# bla is used as variable
bla=i.connect(
    # localhost is important
    host="localhost",
    user="root",
    password="",
    database="python"
)
if bla.is_connected():
    print("yaaaay")
# cursor is a variable
cursor=bla.cursor()
cursor.execute("select * from one")

for i in cursor:
    print(i)
cursor.close()
bla.close()