num = int(input("Enter first no : "))
num2 = int(input("Enter second no : "))

try:
    div = num / num2
    print("{} / {} = {}".format(num, num2, div))
except Exception as e:
    print(str(e))
else:
    print("else part here")
finally:
    print("finally block always execute")


# NOTE : you can also use else : if not exeption then it will execute otherwise not
#  Finally block always excecute
