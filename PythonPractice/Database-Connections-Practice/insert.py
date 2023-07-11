import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.Student values(12,'hello','SatyaSai','AIDS')")
mydb.commit()
mydb.close()