def strReverse():
    fname = input("Enter your first name : ")
    lname = input("Enter your last name : ")

    rev_fname = fname[::-1]
    rev_lname = lname[::-1]
    
    print(rev_fname+" "+rev_lname)

strReverse()