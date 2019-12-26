class Employee:

    def __init__(self, first, last, email):
        self.first = first
        self.last  = last
        self.email = first + "." + last + "@company.com"
    

    def fullname(self):
        return "{} {} ".format(self.first, self.last)
    

emp_obj = Employee("gaurav", "sanas", "100000")
emp_obj2 = Employee("sunil", "pal", "78888")

# print(emp_obj.fullname())

print(Employee.fullname(emp_obj2))
