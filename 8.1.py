import random
import math
P = random.randint(1,5)
print("P =", P)
B = random.randint(1,5)
print("B =", B)
C = random.randint(1,5)
print("C =", C)
A = random.randint(-5,5)
print("A", A)

def Power(A, B):
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))
print("A^P =", round(Power(A, P)))
print("B^P =", round(Power(B, P)))
print("C^P =", round(Power(C, P)))
    
