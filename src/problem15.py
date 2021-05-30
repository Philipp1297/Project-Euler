# Problem 15 Lattice paths
# Formular:
# (2*n)! / (n! * n!)

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact

x= fact(40)
y= fact(20)
erg= x/(y*y)
print(erg)