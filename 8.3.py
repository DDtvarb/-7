
def maxdig(n):
    if n < 10:
        return n
    else:
        return max(n % 10, maxdig(n // 10))

import random
x = random.randint(10000,99999)
print(x)
print(maxdig(x)) 
