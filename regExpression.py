import re

string = "Hello my name is gaurav sanas, I am 27 years old"

match = re.search("27", string)

if match:
    print("match found at position : ", match.start())
else:
    print("not found")

# case sensitive if we used small h it will not match
# ^ start with
match2 = re.search("^Hello", string)

if match2:
    print("match found")
else:
    print("not found")

# Ends with used $

match3 = re.search("old$", string)

if match3:
    print("match found")
else:
    print("not found")


# start with and Ends with used ^ $

match4 = re.search("[^Hello.*old$]", string)

if match4:
    print("match found")
else:
    print("not found")


# findall() 
match5 = re.findall("a", string)

if match5:
    print("match found")
else:
    print("not found")




