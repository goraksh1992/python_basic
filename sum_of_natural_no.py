def naturalNoSum():

    num = int(input("Enter number : "))
    sum = 0
    for x in range(num+1):
        sum = sum + x
    
    print(sum)

naturalNoSum()