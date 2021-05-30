# problem 48 Self powers
erg=0
for i in range(1,1001):
    erg+=i**i
x=str(erg)
print(x[-10:])