# Problem 1 Multiples of 3 and 5
sum([i for i in range(1,1000) if i%3==0 or i%5==0])

# Problem 2 Even Fibonacci numbers
fibonacci_numbers = [0, 1]
for i in range(2,100):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

liste= []
for i in fibonacci_numbers:
    if i < 4000000:
        liste.append(i)

x= sum([i for i in liste if i%2==0 and i>0])

# Problem 3 	Largest prime factor
x = 600851475143
k = 1
while k < x:
    k += 1
    while x % k == 0: 
        x = x // k
#print(k) # k is solution

# Prblem 4 	Largest palindrome product
liste=[]
for i in range(100, 999):
    for j in range(100, 999):
        x= i*j
        if str(x) == str(x)[::-1]:
            liste.append(x)

#print(max(liste))





