import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amaldas@12345",
    database="temp_db",
    port=3304
)

print("Connected successfully!")

mytable = db.cursor()
mytable.execute("select * from Mytable")

for row in mytable:
    print(row)