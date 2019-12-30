def divisibleNo():

    lst = [12, 65, 54, 39, 102, 339, 221]

    lst2 = []
    for x in lst:
        if x % 13 == 0:
            if x not in lst2:
                lst2.append(x)
            else:
                pass
    
    print(lst2)

divisibleNo()