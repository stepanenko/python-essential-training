
# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print()

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
