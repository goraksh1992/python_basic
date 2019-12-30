def fibo():

    num = int(input("Enter no : "))

    first = 0
    second = 1

    print(second)
    for x in range(1, num+1):
        temp = first + second
        print(temp)
        first = second
        second = temp
fibo()