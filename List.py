list1 = [9, 5, 6, 7, 6, 3, 2, 1]
list2 = [17, 55, 39, 46]
list3 = ['t', 'y', 'p', 'e', 'w', 'r', 'i', 't', 'e', 'r']
tuple1 = (1, 5, 7, 9)
set1 = {6, 2, 3}

# REPETITION
x = list1*2
print(x)        # [9, 5, 6, 7, 6, 3, 2, 1, 9, 5, 6, 7, 6, 3, 2, 1]

# CONCATENATION
x = list1+list2
print(x)        # [9, 5, 6, 7, 6, 3, 2, 1, 17, 55, 39, 46]

# MEMBERSHIP
print(6 in list1)   # True

# ITERATION
for i in list1:
    print(i)
'''
9
5
6
7
6
3
2
1
'''

# LENGTH
x = len(list1)      # list1 = [9, 5, 6, 7, 6, 3, 2, 1]
print(x)            # 8

# MAXIMUM VALUE OF ANY DATA TYPE
x = max(list3)      # list3 = ['t', 'y', 'p', 'e', 'w', 'r', 'i', 't', 'e', 'r']
print(x)            # y

# MINIMUM VALUE OF ANY DATA TYPE
x = min(list1)      # list1 = [9, 5, 6, 7, 6, 3, 2, 1]
print(x)            # 1


# BUILT-IN OPERATIONS

list2 = [17, 55, 39, 46]

# 1. UPDATE
list2[3] = 19
print(list2)        # [17, 55, 39, 19]

# 2. APPEND (ADDS AT THE END)

list2.append(9)
print(list2)    # [17, 55, 39, 19, 9]

list2.append(list1)
print(list2)    # [17, 55, 39, 19, 9, [9, 5, 6, 7, 6, 3, 2, 1]]

list2.append(tuple1)
print(list2)    # [17, 55, 39, 19, 9, [9, 5, 6, 7, 6, 3, 2, 1], (1, 5, 7, 9)]

list2.append(set1)
print(list2)    # [17, 55, 39, 19, 9, [9, 5, 6, 7, 6, 3, 2, 1], (1, 5, 7, 9), {2, 3, 6}]


# 3. INSERT (CAN ADD USING INDEX NUMBER)

list2 = [17, 55, 39, 46]        # REASSIGNING VALUES OF LIST 2

list2.insert(3, 'hi')
print(list2)            # [17, 55, 39, 'hi', 46]

list2.insert(4, tuple1)
print(list2)            # [17, 55, 39, 'hi', (1, 5, 7, 9), 46]


# 4. EXTENDS (ADD EVERYTHING AS AN ELEMENT OF LIST)

list2 = [17, 55, 39, 46]        # REASSIGNING VALUES OF LIST 2

list1.extend(list2)
print(list1)    # [9, 5, 6, 7, 6, 3, 2, 1, 17, 55, 39, 46]

list2.extend(tuple1)
print(list2)    # [17, 55, 39, 46, 1, 5, 7, 9]

# --------------------------------------------------------------------------------- #

# 5. DELETE (USES INDEX NUMBER AND SLICING OPERTOR)

list2 = [17, 55, 39, 46]        # REASSIGNING VALUES OF LIST 2

del list2[1:2]
print(list2)   # [17, 39, 46]


# 6. REMOVE (USES DIRECT ELEMENT)

list2 = [17, 55, 39, 46]        # REASSIGNING VALUES OF LIST 2

list2.remove(39)
print(list2)    # [17, 55, 46]


# 7. POP(USES INDEX NUMBER AND IF NOT DEFINED REMOVES LAST ELEMENT)

list2 = [17, 55, 39, 46]        # REASSIGNING VALUES OF LIST 2

list2.pop(0)
print(list2)    # [55, 39, 46]
list2.pop()
print(list2)    # [55, 39]


# --------------------------------------------------------------------------------- #


# 8. CLEAR (RETURNS EMPTY LIST)

list2 = [17, 55, 39, 46]            # REASSIGNING VALUES OF LIST 2

list.clear(list2)
print(list2)    # []

# 9. COPY (COPIES THE ELEMENT)

list2 = [17, 55, 39, 46]            # REASSIGNING VALUES OF LIST 2

list4 = []
list4 = list2.copy()
print(list4)       # [17, 55, 39, 46]

# 10. COUNT (COUNTS THE NUMBER OF OCCURENCE)
x = list3.count('t')    # list3 = ['t', 'y', 'p', 'e', 'w', 'r', 'i', 't', 'e', 'r']
print(x)    # 2

# 11. INDEX (INDEX OF THE ELEMENT)
x = list3.index('e', 2, 9)
print(x)    # 3
x = list2.index(55)
print(x)    # 1


# 12. SORT(ARRANGES FROM ASCENDING TO DESCENDING)

list2 = [17, 55, 39, 46]            # REASSIGNING VALUES OF LIST 2

list1.sort()
print(list1)    # [1, 2, 3, 5, 6, 6, 7, 9, 17, 39, 46, 55]
list2.sort()
print(list2)    # [17, 39, 46, 55]


# 13. REVERSE (REVERSES THE LIST WITHOUT SORTING)

list2 = [17, 55, 39, 46]            # REASSIGNING VALUES OF LIST 2

list1.reverse()
print(list1)        # [55, 46, 39, 17, 9, 7, 6, 6, 5, 3, 2, 1]
list2.reverse()
print(list2)        # [46, 39, 55, 17]


