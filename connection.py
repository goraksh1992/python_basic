import mysql.connector

class MysqlConnection:

    def __init__(self):

        self.mydb = mysql.connector.connect(

            host     = "localhost",
            user     = "root",
            passwd   = "",
            database = "mypython"
        )

        self.mycursor = self.mydb.cursor()