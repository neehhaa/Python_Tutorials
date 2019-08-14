tuple1 = ('t', 'e', 'l', 'e', 'p', 'a', 't', 'h', 'y')
tuple2 = ('a', 'p', 'p', 'l', 'e')

x = tuple1+tuple2       # CONCATENATION
print(x)                # ('t', 'e', 'l', 'e', 'p', 'a', 't', 'h', 'y', 'a', 'p', 'p', 'l', 'e')

x = tuple2*2            # REPETITION
print(x)                # ('a', 'p', 'p', 'l', 'e', 'a', 'p', 'p', 'l', 'e')

x = max(tuple1)         # RETURNS MAXIMUM VALUE
print(x)                # y

x = min(tuple1)         # RETURNS MINIMUM VALUE
print(x)                # a

x = len(tuple2)         # RETURNS LENGTH OF THE TUPLE
print(x)                # 5

x = tuple2.count('p')   # RETURNS COUNT OF AN ELEMENT IN TUPLE
print(x)                # 2

x = tuple1.index('a')   # RETURNS INDEX OF AN ELEMENT IN TUPLE
print(x)                # 5

print('a' in tuple1)    # MEMBERSHIP (True)

# LIST IN TUPLE ARE MUTABLE

tuple3 = (3, 3, 2, 6, 5, 4, [5, 66, 5, 4, 8, 9])

tuple3[6][2] = 44
print(tuple3)           # (3, 3, 2, 6, 5, 4, [5, 66, 44, 4, 8, 9])

