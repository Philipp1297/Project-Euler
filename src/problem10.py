y= sum([x for x in range(1, 2000001) if all(x % y != 0 for y in range(2, x))])
print(y-1)