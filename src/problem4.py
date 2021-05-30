# Prblem 4 Largest palindrome product

liste=[]
for i in range(100, 999):
    for j in range(100, 999):
        x= i*j
        if str(x) == str(x)[::-1]:
            liste.append(x)

#print(max(liste))