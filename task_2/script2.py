from functions import *

print("x y z f")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = equivalence(x, z) or inquest(x, y and z)
            if f == 0:
                print(f'{x} {y} {z} {f}')
