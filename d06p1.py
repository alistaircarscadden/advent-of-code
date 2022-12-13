from common import *

al = inf_lstrip()
l = al[0]
for i in range(len(l) - 4):
    a, b, c, d = l[i : i + 4]
    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(i + 4)
        break
