from common import *

al = inf_lstrip()
l = al[0]
for i in range(len(l) - 14):
    c = l[i : i + 14]
    cool = True
    for j in range(14):
        for k in range(j + 1, 14):
            if c[j] == c[k]:
                cool = False
                break
        if not cool:
            break
    if cool:
        print(i + 14)
        break
