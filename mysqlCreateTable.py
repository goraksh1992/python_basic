import mysql.connector

mydb = mysql.connector.connect(

    host   = "localhost",
    user   = 'root',
    passwd = "",
    database = "mypython"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE custoners (name varchar(20), address varchar(500))")
