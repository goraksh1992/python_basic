def generateListTouples():
    assets = input("Enter comma-separated numbers : ")

    lst = []
    tpl = ()
    for x in assets:
        if x == ",":
            pass
        else:
            lst.append(x)
    
    for x in assets:
        if x == ",":
            pass
        else:
            tpl += tuple(x)

    print("list =", lst)
    print("\n")
    print("Touple =", tpl)

generateListTouples()


# or

# list = assets.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
    
