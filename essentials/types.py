
# Python has 4 built-in data types to store collections of data:
# Tuple, List, Set, and Dictionary, all with different qualities and usage.

# Tuple is a collection which is ordered, unchangeable and allow duplicates:
# Unchangeable - cannot change, add or remove items after the tuple has been created.
myTuple = (5, 7, 7, '8', 'great')
print('myTuple is {}'.format(myTuple))
print(type(myTuple))  # <class 'tuple'>


# List items are indexed, ordered, changeable, and allow duplicate values:
myList = ["apple", "banana", "cherry"]
print('myList is {}'.format(myList))
print(type(myList))  # <class 'list'>


# Set is a collection which is unordered, unindexed, unchangeable (but you can add items):
# Sets cannot have two items with the same value:
mySet = {"apple", "banana", "cherry", "cherry"}
print('mySet is {}'.format(mySet))
# mySet is {'banana', 'apple', 'cherry'}
print(type(mySet))  # <class 'set'>


# Dictionary is a collection which is ordered, changeable and does not allow duplicates:
myDict = {'a': 5, 'a': 7, 'c': 8}
print('myDict is {}'.format(myDict))
print(type(myDict))  # <class 'dict'>


# Python has the following data types built-in by default, in these categories:

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview

# Setting the Specific Data Type:
# https://www.w3schools.com/python/python_datatypes.asp

x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

# Output:
# x is <class 'str'>
# x is 47
# y is <class 'int'>
# y is 47
