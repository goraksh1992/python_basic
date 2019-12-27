lst = [4,8,0,7,8]

my_lst = iter(lst)

print(next(my_lst))

print(next(my_lst))

## next(obj) is same as obj.__next__()

print(my_lst.__next__())
print(my_lst.__next__())
print(my_lst.__next__())

next(my_lst) # it will return errot with StopIteration no iteration is remaining