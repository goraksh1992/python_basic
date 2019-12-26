import sqlite3 as lite

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect("course.db")
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create DB!")
    
    # TODO : Insert data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            return False
    
    # TODO : Fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
    
    # TODO : Delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE Id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


# TODO : User interface
def main():

    db = DatabaseManage()

    print("*"*40)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    print("\n")

    print("Press 1. Insert new course \n")
    print("Press 2. Show all courses \n")
    print("Press 3. Delete course (Enetr course id) \n")

    print("#"*40)
    print("\n")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        name = input("Enter course name : ")
        description = input("Enter course description : ")
        price = input("Enter course price : ")
        is_private = input("Is this course is private (0/1) : ")

        if db.insert_data([name, description, price, is_private]):
            print("Course added successfully")
        else:
            print("Oops Something is wrong")

    elif choice == "2":
        print("\n :: Course List :: \n")

        for index, item in enumerate(db.fetch_data()):
            print("Sl no " + str(index + 1))
            print("Course Id " + str(item[0]))
            print("Course name " + str(item[1]))
            print("Course description " + str(item[2]))
            print("Course price " + str(item[3]))
            private = "Yes" if item[4] else "No"
            print("Is private " + str(private))
            print("\n")
    
    elif choice == "3":
        
        id = input("Enter course id to delete : ")
        if db.delete_data(id):
            print("Course deleted successfully")
        else:
            print("Oops Something is wrong")

    else:
        print("\n Bad Choice")

if __name__ == "__main__":
    main()