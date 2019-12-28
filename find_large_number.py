def maxNumber():

    count = int(input("Enter how many number : "))
    lst = []

    for x in range(count):
        if(x <= count):
            num = int(input("Enter number {}: ".format(x+1)))
            lst.append(num)
    temp = 0
    for o in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[o] > lst[j+1]:
                if temp > lst[o]:
                    pass
                else:
                    temp = lst[o]                
            else:
                pass
    print("max number is : {}".format(temp))
    
maxNumber()
