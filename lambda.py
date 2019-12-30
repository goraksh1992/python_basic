def sumOfDigit(a, b):

    x = lambda a, b : a + b
    return x(a, b)

num = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("sum is {}".format(sumOfDigit(num, num2)))