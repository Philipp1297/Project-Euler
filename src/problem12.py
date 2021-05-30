# Poblem 12 Highly divisible triangular number

import math

def countfactors(num):
    factors = 0
    for x in range(1,int(math.sqrt(num))+1):
        if num % x == 0:
            factors +=2
    return factors

seed = 1

y = True
while y: 
    seed += 1
    if seed % 2 == 0:
        factors = countfactors(seed/2)*countfactors(seed+1)
    else:
        factors = countfactors(seed)*countfactors((seed+1)/2)
    if factors > 500: break
        

print(seed*(seed+1)/2)