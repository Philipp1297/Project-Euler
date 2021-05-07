# Problem 14

liste=[]
ergListe = []
listeZahlen = []
x=0
for i in range(14,1000000):
    listeZahlen.append(i)
    x=i
    liste.append(x)
    while x>1:
        if i%2==0:
            x=x/2
            liste.append(x)
        else:
            x=((3*x)+1)
            liste.append(x)
    ergListe.append(len(liste))

max_value = max(ergListe)
max_index = ergListe.index(max_value)
wert = listeZahlen[max_index]

print(max_value)
print(max_index)
print(wert)