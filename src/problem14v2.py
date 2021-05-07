cache = {1: 1}
def collatz_count(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + collatz_count(n / 2)
        else:
            cache[n] = 1 + collatz_count(3 * n + 1)
    return cache[n]

liste = []
liste2 = []
for i in range(1,100000):
    liste.append(i)
    liste2.append(collatz_count(i))

max_value = max(liste2)
print(liste[max_value])


