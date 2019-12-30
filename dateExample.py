import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)

# Show weekday in full version
print(x.strftime("%A"))
# Show weekday in short version 
print(x.strftime("%a"))
# Show month name in full version
print(x.strftime("%B"))
# Show month name in short version
print(x.strftime("%b"))
# Show year name in full version
print(x.strftime("%Y"))
# Show year name in short version
print(x.strftime("%y"))
# Show hourse time
print(x.strftime("%H"))
# Show minute time
print(x.strftime("%M"))
# Show second time
print(x.strftime("%S"))
# Show AM/PM time 
print(x.strftime("%p"))