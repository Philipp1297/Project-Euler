# Problem 9 Special Pythagorean triplet
for i in range(0,1000):
    for j in range(0,1000):
        for k in range(0,1000):
            if i<j<k:
                if ((i*i + j*j) == k*k):
                    if i+j+k==1000:
                        print(i," ",j," ",k)
                        print(i*j*k)
