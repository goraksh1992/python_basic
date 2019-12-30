def gcd():

    num = int(input("Enter first no : "))
    num2 = int(input("Enter second no : "))

    lst = []
    lst2 = [] 

    if num == 0 or num2 == 0:
        print("number must greater than 0")
    else:
        for x in range(1, num+1):
            if num % x == 0:
                if x not in lst:
                    lst.append(x)
        
        for x2 in range(1, num2+1):
            if num2 % x2 == 0:
                if x2 not in lst2:
                    lst2.append(x2)

    lst3 = list(set(lst).intersection(lst2))

    print("GCD of {} and {} is {}".format(num, num2, max(lst3)))

gcd()
                