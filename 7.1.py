import random
import numpy 
M = random.randrange(2,10)
N = random.randrange(2,10)
K = random.randrange(1,N)
print("M = ",M,"; N = ",N,"; K = ",K+1)
a = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        a[i][j] = random.randrange(-5,5)
print(a)
print("Cтолбец ",K+1,": ")
for i in range(M):
    print(a[i][K])
print()

