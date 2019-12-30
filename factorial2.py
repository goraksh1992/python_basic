def cal_factorial(n):

    if(n == 1):
        return n
    else:
        return (n * cal_factorial(n-1))
    

result = cal_factorial(5)
print(result)