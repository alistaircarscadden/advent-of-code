from common import *

ag = listsplit(inf_lstrip(), "")

bsum = 0

for g in ag:
    g = [int(x) for x in g]
    gsum = sum(g)
    bsum = max(gsum, bsum)

print(bsum)
