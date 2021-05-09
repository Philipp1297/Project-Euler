# Problem 19 Countin Sundays

# Leap years
listLeap=[] 
listNoLeap=[]
for i in range(1900,2001):
    if i % 4 ==0 and not i%400==0:
        listLeap.append(i)
    else:
        listNoLeap.append(i)


# days between 1900 to 2000



