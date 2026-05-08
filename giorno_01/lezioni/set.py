# Creating Sets

fruits = {'apple', 'banana', 'mango'}
print(fruits)

numbers = {1, 2, 2, 3}
print(numbers)   # duplicates removed

# Length

print(len(fruits))

# Checking Item

print('apple' in fruits)   # True


# Adding Items

fruits.add('orange')
print(fruits)


# Removing Items

fruits.remove('banana')
print(fruits)

# Joining Sets

A = {1, 2}
B = {3, 4}

print(A.union(B))


# Common Items

X = {1, 2, 3}
Y = {2, 3, 4}

print(X.intersection(Y))   # {2, 3}