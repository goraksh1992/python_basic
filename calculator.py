class Calculator:

    def __init__(self):
        pass
        # self.number1 = number1
        # self.number2 = number2
        # self.operation = operation
    
    # add two number
    def addNumber(self, number1, number2):
        add = number1 + number2
        return "{} + {} = {}".format(number1, number2, add)
    
    # Substract two number
    def subNumber(self, number1, number2):
        sub = number1 - number2
        return "{} - {} = {}".format(number1, number2, sub)
    
    # Multiply two number
    def multNumber(self, number1, number2):
        mult = number1 * number2
        return "{} * {} = {}".format(number1, number2, mult)
    
    # Division two number
    def divNumber(self, number1, number2):
        try:
            div = number1 / number2
            return "{} / {} = {}".format(number1, number2, div)
        except Exception:
            return "Divison not possible"

def main():

    obj = Calculator()

    print("#"*50)
    print("\n Enter your choice \n")
    print("#"*50)
    print("\n")
    print("1. Addition \n")
    print("2. Substract \n")
    print("3. Multiply \n")
    print("4. Division \n")
    print("#"*50)
    print("\n")

    print("#"*50)
    print("\n Operation \n")
    print("#"*50)
    print("\n")
    first  = int(input("Enter first no : "))
    second = int(input("Enter second no : "))
    oprt   = input("Enter operation : ")
    print("#"*50)
    print("\n")

    if oprt == "1":
        print(obj.addNumber(first, second))
    elif oprt == "2":
        print(obj.subNumber(first, second))
    elif oprt == "3":
        print(obj.multNumber(first, second))
    else:
        print(obj.divNumber(first, second))

if __name__ == "__main__":
    main()
    