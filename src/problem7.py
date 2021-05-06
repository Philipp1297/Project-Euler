
y= [x for x in range(1, 20000) if all(x % y != 0 for y in range(2, x))]
print(y)