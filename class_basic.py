class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

blu = Parrot("blu", 10)
woo = Parrot("woo", 12)

# Access class attributes
print("blu is a {}".format(blu.__class__.species))
print("blu is also a {}".format(woo.__class__.species))

# Access instance attributes
print("{} age is {}".format(blu.name, blu.age))
print("{} age is {}".format(woo.name, woo.age))