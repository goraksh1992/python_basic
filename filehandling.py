#  Read file
# f = open("demofile.txt", 'r')
# print(f.read(5))
# print(f.readline())

#  Append file
# f = open("demofile.txt", 'a')
# f.write("\nThis is my new line\n")
# f.close()
# f = open("demofile.txt")
# print(f.read())

# For write file
# f = open("demofile.txt", 'w')
# f.write("oops all record deleted")
# f.close()

# f = open("demofile.txt")
# print(f.read())

# Create file
# try:
#     f = open('demofile1.txt', 'x')
#     f.write("This is new created fiel")
#     f.close()
# except Exception as e:
#     f = open('demofile1.txt')
#     print(f.read()) 

# Delete file
import os
os.remove("demofile1.txt")

