# Problem 20 Factorial digit sum

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact

x= fact(100)
x=str(x)
erg=0
for i in x:
    erg+=int(i)

print(erg)