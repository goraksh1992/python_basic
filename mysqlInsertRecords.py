import connection

class AddCustomerRecord(connection.MysqlConnection):

    def __init__(self):
        pass
        connection.MysqlConnection.__init__(self)
    
    def addCustomer(self, data):

        try:
            self.mycursor.executemany("INSERT INTO custoners (name, address) VALUES (%s,%s)", data)
            self.mydb.commit()
            return True
        except:
            return False
    
    def updateCustomer(self, cust_id, name, address):

        try:
            self.mycursor.execute("UPDATE custoners SET name = %s, address = %s WHERE id = %s", (name, address, cust_id))
            self.mydb.commit()
            return True
        except Exception:
            return False
    
    def deleteCustomer(self, cust_id):
        try:
            self.mycursor.execute("DELETE FROM custoners WHERE id = %s", (cust_id,))
            self.mydb.commit()
            return True
        except Exception:
            return False
    
    def showCustomer(self):

        self.mycursor.execute("SELECT * FROM custoners")
        myresult = self.mycursor.fetchall()
        return myresult
            

def main():

    obj = AddCustomerRecord()

    print("*"*30)
    print("Enter choice")
    print("*"*30)   
    print("1. Add Customer")
    print("2. Update Customer")
    print("3. Delete Customer")
    print("4. Show Customer")
    print("*"*30)

    oprt  = int(input("Enter your choice : "))

    data = []
    if oprt == 1:
        count = int(input("How many record you want insert : "))
        for x in range(count):
            name    = input("Enter customer name : ")
            address = input("Enter customer address  :")
            data.append((name, address))

        if obj.addCustomer(data):
            print("Customer added successfully!")
        else:
            print("Please try again")
    elif oprt == 2:

        cust_id = int(input("Enter customer id : "))
        name    = input("Enter customer name : ")
        address = input("Enter customer address  :") 

        if obj.updateCustomer(cust_id, name, address):
            print("Customer details updated successfully!")
        else:
            print("Please try again")
    
    elif oprt == 3:
        cust_id = int(input("Enter customer id : "))

        if obj.deleteCustomer(cust_id):
            print("Customer deleted successfully")
        else:
            print("Please try again")
            
    else:
        result = obj.showCustomer()
        for records in result:
            print(records)



if __name__ == "__main__":
   main()


