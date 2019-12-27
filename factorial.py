class Factorial:

    def __init__(self, number):
        self.number = number
    
    def factor(self):
        fact = 1
        for x in range(1, self.number+1):
            fact = x * fact
        return "factorial of {} is {}".format(self.number, fact)

num = int(input("Enter number : "))
obj = Factorial(num)
print(obj.factor())