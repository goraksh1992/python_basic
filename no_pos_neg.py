def checkNumber():

    num = int(input("Enter number : "))

    if num > 0:
        print("{} is positive".format(num))
    elif num < 0:
        print("{} is negative".format(num))
    else:
        print("no is zero")

checkNumber()