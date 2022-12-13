from common import *

ag = listchunks(inf_lstrip(), 3)


def priority(c):
    return convert(LOWERCASE, list(range(1, 99)), c) or convert(
        UPPERCASE, list(range(27, 99)), c
    )


w = []
cnt = 0
for g in ag:
    a, b, c = map(set, g)
    z = a.intersection(b).intersection(c).pop()
    z = priority(z)
    w.append(z)

    cnt += 3

print(sum(w))
