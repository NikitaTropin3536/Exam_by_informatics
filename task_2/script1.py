from functions import *

print("x y z f")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = inquest(x or y, equivalence(z, x))
            if f == 0:
                print(f'{x} {y} {z} {f}')
