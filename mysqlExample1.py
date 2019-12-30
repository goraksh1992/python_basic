import mysql.connector

mydb = mysql.connector.connect(

    host   = "localhost",
    user   = "root",
    passwd = ""
)

# to run query we have to must create cursor()

mycursor = mydb.cursor()

#create datbase if not exits 
mycursor.execute("CREATE DATABASE IF NOT EXISTS mypython")
