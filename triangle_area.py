def triangleArea():

    height = int(input("Enter triangle height : "))
    base   = int(input("Enter triangle base : "))
    
    area = (height * base) / 2

    print("Area of triangle is {}". format(area))


triangleArea()