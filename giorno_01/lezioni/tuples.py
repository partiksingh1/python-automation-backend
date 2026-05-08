empty_tuple = ()
empty_tuple2 = tuple()

# fruits = ('banana', 'orange', 'mango', 'lemon')
# print(len(fruits))

# Slicing in tuples (1st is inclusive 2nd is exclusive) 
# middle_two_items = fruits[1:3]
# print(middle_two_items)

# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')