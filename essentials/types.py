
# Python has 4 built-in data types to store collections of data:
# Tuple, List, Set, and Dictionary, all with different qualities and usage.

# Tuple is a collection which is ordered and unchangeable:
t = (5, 7, '8', 'great')
print('t is {}'.format(t))
print(type(t))
# t is 7
# <class 'tuple'>

# Dictionary is a collection which is ordered, changeable and does not allow duplicates:
d = {'a': 5, 'a': 7, 'c': 8}
print('d is {}'.format(d))
print(type(d))
# d is {'a': 7, 'c': 8}
# <class 'dict'>

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
