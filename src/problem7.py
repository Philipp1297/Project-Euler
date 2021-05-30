#Problem 7 10001st prime

y= [x for x in range(1, 200000) if all(x % y != 0 for y in range(2, x))][10001]
print(y)