lst = [4,8,0,7,8]

my_lst = iter(lst)

print(next(my_lst))

print(next(my_lst))

## next(obj) is same as obj.__next__()

print(my_lst.__next__())
print(my_lst.__next__())
print(my_lst.__next__())

# next(my_lst) # it will return errot with StopIteration no iteration is remaining


lst2 = [7,8,2,4,2,5,7]

my_lst2 = lst2.__iter__()

print(my_lst2.__next__())