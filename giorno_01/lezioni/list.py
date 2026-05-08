# 1. Creating Lists

empty_list = []
print(len(empty_list))   # 0

fruits = ['apple', 'banana', 'mango']
numbers = [1, 2, 3, 4]

print(fruits)
print(len(fruits))       # number of items


# 2. Accessing Items

colors = ['red', 'blue', 'green', 'yellow']

print(colors[0])     # first item
print(colors[1])     # second item

print(colors[-1])    # last item
print(colors[-2])    # second last item


# 3. Slicing Lists

animals = ['cat', 'dog', 'lion', 'tiger', 'elephant']

print(animals[0:3])   # ['cat', 'dog', 'lion']
print(animals[2:])    # from index 2 to end
print(animals[:3])    # first 3 items
print(animals[-3:])   # last 3 items


# 4. Changing Items

cars = ['BMW', 'Toyota', 'Ford']

cars[0] = 'Tesla'
print(cars)

cars[-1] = 'Honda'
print(cars)


# 5. Checking Items

foods = ['rice', 'pizza', 'burger']

print('pizza' in foods)   # True
print('pasta' in foods)   # False


# 6. Adding Items

students = ['John', 'Mary']

# append() -> add at the end
students.append('David')
print(students)

# insert() -> add at specific position
students.insert(1, 'Sarah')
print(students)


# 7. Removing Items

letters = ['a', 'b', 'c', 'd']

# remove by value
letters.remove('b')
print(letters)

# pop() removes last item
letters.pop()
print(letters)

# pop(index)
letters.pop(0)
print(letters)

# del removes using index
nums = [10, 20, 30]
del nums[1]
print(nums)

# clear() removes everything
nums.clear()
print(nums)


# 8. Copying Lists

original = ['pen', 'book']
copy_list = original.copy()

print(copy_list)

# 9. Joining Lists

list1 = [1, 2]
list2 = [3, 4]

# using +
joined = list1 + list2
print(joined)

# using extend()
list1.extend(list2)
print(list1)


# 10. Counting Items


ages = [20, 21, 20, 22, 20]

print(ages.count(20))   # 3

# 11. Finding Index

languages = ['Python', 'Java', 'C++']

print(languages.index('Java'))   # 1

# 12. Reverse List

names = ['Ali', 'John', 'Mike']

names.reverse()
print(names)

# 13. Sorting Lists

scores = [50, 10, 80, 30]

# ascending order
scores.sort()
print(scores)

# descending order
scores.sort(reverse=True)
print(scores)