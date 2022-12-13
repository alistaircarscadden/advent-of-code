from common import *
from itertools import zip_longest


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return -1
        if a < b:
            return 1
    elif isinstance(a, list) and isinstance(b, list):
        for a, b in zip_longest(a, b, fillvalue=None):
            if a is None:
                return 1
            elif b is None:
                return -1
            else:
                r = compare(a, b)
                if r != 0:
                    return r
    else:
        if isinstance(a, int):
            return compare([a], b)
        else:
            return compare(a, [b])
    return 0


gs = listsplit(inf_lstrip(), "")

s = 0
for i, g in enumerate(gs):
    a = eval(g[0])
    b = eval(g[1])
    if compare(a, b) == 1:
        s += i + 1
print(s)
