import random
import numpy 
M = random.randrange(2,10)
N = random.randrange(2,10)
print("M = ",M,"; N = ",N)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,5)
print(a)
print('__________________________________')
direction = 1
for j in range(N):
    for i in range(M):
        if direction == 1:
            print(a[i][j], end=" ")
            #a[i][j] = a[i][j]
        else:
            print(a[M-1-i][j], end=" ")
            #a[i][j] = a[M-1-i][j]
            
    direction *= -1
#print(a)








