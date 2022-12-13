from common import *

al = inf_lstrip()


def priority(c):
    return convert(LOWERCASE, list(range(1, 99)), c) or convert(
        UPPERCASE, list(range(27, 99)), c
    )


w = []
for l in al:
    s = len(l)
    a = l[: s // 2]
    b = l[s // 2 :]
    A = set(a)
    B = set(b)
    w.append(priority(A.intersection(B).pop()))

print(sum(w))
