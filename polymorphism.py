class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can not swin")
    

class Penguin:

    def fly(self):
        print("Penguin can not fly")
    
    def swim(self):
        print("Penguin can swim")

def flying_test(obj):
    obj.fly()

blu = Parrot()
woo = Penguin()

flying_test(blu)
flying_test(woo)