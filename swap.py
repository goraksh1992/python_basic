def swap():

    num = int(input("Enter first no : "))
    num2 = int(input("Enter second no : "))

    print("before swap num = {} and num2 = {}".format(num, num2))
    
    temp = 0

    temp = num
    num  = num2
    num2 = temp

    print("After swap num = {} and num2 = {}".format(num, num2))

swap()