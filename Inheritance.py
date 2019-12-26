class Bird:

    def __init__(self):
        print("Bird class")
    
    def whoIsThis(self):
        print("bird")
    
    def swim(self):
        print("swim")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin class")
    
    def whoIsThis(self):
        print("penguin")
    
    def run(self):
        print("run fast")


# Create penguin class instance
peggy = Penguin()
# Create bird class instance
brd = Bird()
# Call method here
brd.whoIsThis()
peggy.whoIsThis()
peggy.swim()
peggy.run()