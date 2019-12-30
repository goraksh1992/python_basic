def listMethod():
    #  List methods

    lst = [5,7,15,11,55,"gaurav",4.4,1.01]

    print("Original list : ", lst)

    # append() : used to append element in string at end
    lst.append("php")

    print("After append list is : ", lst)

    # extends() : Add Elements of a List to Another List
    lst2 = [44,55,77,11]
    lst3 = [77,11,55,99]

    lst2.extend(lst3)

    print(lst2) 
    # Duplicate value also accepted

    # Insert() : insert element in list with position
    lst.insert(1, "hello")

    print(lst)

    # remove() : Remove element from the list pass element name
    lst.remove("hello")

    print(lst)

    # index() : Return index of element
    print("position of gaurav in list is : ",lst.index("gaurav"))

    # count() : Count occurence of specific element in list
    print("11 occure {} time in list ".format( lst.count(11)))

    # pop() : Remove last or return last element and also pass the position
    print(lst.pop()) 
    print("after removing last element lis is ", lst)

    # reverse() : sort list in reverse order
    lst.reverse()
    print(lst)

    # sort() : sort list
    lst5 = [5,921,1,855,255,777]
    lst5.sort()
    print("Sort in asending : ", lst5)
    lst5.sort(reverse=True)
    print("Sort in desending : ", lst5)

    # copy() : copy one list to another list
    lst6 = lst.copy()
    print("Copy list is : ", lst6)

    # clear() : delete all element in list
    lst6.clear()
    print(lst6)

    # len() : find the lenth of list
    print(len(lst))

    lst7 = [44,88,66,121,744,55]
    # max() : find maximum value in list
    print(max(lst7))

    # min() : find minimum value
    print(min(lst7))

    # slice() : 

    print(slice(3))
    print(slice(1,3))
    print(slice(1,5,2))

    pyString = 'Python'
    # contains indices (0, 1, 2)
    # i.e. P, y and t
    sObject = slice(3)
    print(sObject)
    print(pyString[sObject])



listMethod()
