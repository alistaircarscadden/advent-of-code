from common import *

ag = listsplit(inf_lstrip(), "")

sums = []

for g in ag:
    g = [int(x) for x in g]
    gsum = sum(g)
    sums.append(gsum)

sums.sort()
fsum = sum(sums[-3:])
print(fsum)
