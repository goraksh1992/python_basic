def armstrong():

    num = int(input("Enter number : "))

    temp = num
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum += rem **3
        temp //= 10

    if num == sum:
        print("Amstrong number")
    else:
        print("not amstrong number") 

armstrong()