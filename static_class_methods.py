class Employee:

    rise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay  
        self.email = first +"."+ last + "@company.com"

    # Regular method
    def fullname(self):
        print("{} {}".format(self.first, self.last))
    
    # Class method
    @classmethod
    def set_rise_amount(cls, amount):
        cls.rise_amt = amount
    
    @classmethod
    def from_string(cls, string):
        first, last, amount = string.split("-")
        return "{} {} have {} salary ".format(first, last, amount)
    
    @classmethod
    def from_string2(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, pay)



obj = Employee("gaurav", "sanas", 70000)

obj.fullname()

print(Employee.from_string("gaurav-sansa-100000"))

str_emp = "gaurav-sanas-45200"
emp1 = Employee.from_string2(str_emp)
print(emp1.first)
print(emp1.pay)

