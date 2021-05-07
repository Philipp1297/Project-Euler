import time

start = time.time()

def collatz(n):

    counter = 1
    while n>1:
        if n%2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n+1
            counter += 1
        if n == 1:
            return counter
largest_number = 0

large_seq = 0

#for loop for 1 million
for i in xrange(1000000,1,-1):
 #size of collatz for the iteration
 n = collatz(i)
 #if size if greater than previous
 #replace it with the new one
 if n > large_seq:
  largest_number = i
  large_seq = n

#printing the largest number
print largest_number

#time at the end of execution
end = time.time()

#Printing the total time taken
print end-start