def primeNumber():
    
    num = int(input("Enter number : "))

    lst = []
    for x in range(1, num+1):
        for n in range(1, x+1):
           if n % 2 == 0:
                if n not in lst:
                   lst.append(n)
                else:
                    pass
    print(lst) 

primeNumber()