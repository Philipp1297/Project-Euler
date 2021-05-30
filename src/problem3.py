# Problem 3 Largest prime factor

x = 600851475143
k = 1
while k < x:
    k += 1
    while x % k == 0: 
        x = x // k
#print(k) # k is solution