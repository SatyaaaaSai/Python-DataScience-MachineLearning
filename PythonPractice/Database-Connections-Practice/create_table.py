import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE  if not EXISTS test1.Student_data(sno INT,id VARCHAR(10),Name VARCHAR(30),Branch VARCHAR(20))")
mydb.close()