class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    #  Two object addition
    def __add__(self, other):
        obj1 = self.x + other.x
        obj2 = self.y + other.y
        return "({},{})".format(obj1, obj2)
    
    # Two object multiplication
    def __mul__(self, other):
        obj1 = self.x * other.x
        obj2 = self.y * other.y
        return "({},{})".format(obj1, obj2)
    
    #  Two object division
    def __truediv__(self, other):
        obj1 = self.x / other.x
        obj2 = self.y / other.y
        return "({},{})".format(obj1, obj2)
    
    # Compaire two object
    def __lt__(self, other):
        obj1 = self.x + other.x
        obj2 = self.y + other.y
        return obj1 < obj2
    


obj = Point(10,20)
obj1 = Point(2, 5)

# print(obj)

# Operator overloading
print(obj + obj1)
print(obj * obj1)
print(obj / obj1)

# Comparision operator overloading
print(obj < obj1)

# NOTE : We can not do operation two or more object directly to do this we used special functions in python
# like __add__() : add two objects, __sub__(), __mul__(), __truediv__() etc.
# Comparision operator : __lt__(), __gt__(), __ge__(), __le__() etc.