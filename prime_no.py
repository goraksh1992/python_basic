class PrimeNumber:

    def __init__(self, number):
        self.number = number
    
    def primeNo(self):
        for x in range(self.number):
            if self.number % 2 == 0:
                break
            return True
        return False

x = int(input("Enter number : "))
obj = PrimeNumber(x)

result = obj.primeNo()
if result:
    print("{} Number is prime".format(x))
else:
    print("{} Number is not prime".format(x))
    

        