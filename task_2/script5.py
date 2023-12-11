from functions import *

print("y w z x")
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = (inquest(x, y) and inquest(y, w)) or equivalence(z, x or y)
                if f == 0:
                    print(f'{y} {w} {z} {x}')
