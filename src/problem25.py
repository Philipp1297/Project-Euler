# Problem 25 1000-digit Fobonacci number

liste = [0,1]
i = 2

while True:
	liste_new = liste[i-1]+liste[i-2]
	liste.append(liste_new)
	if liste_new>10**999:
		print(i)
		break
	i = i+1

