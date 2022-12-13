from common import *
from itertools import zip_longest
import functools


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


a = [[2]]
b = [[6]]
al = [eval(l) for l in inf_lstrip() if l]
al.append(a)
al.append(b)
al.sort(key=functools.cmp_to_key(compare))
al.reverse()
print((al.index(a) + 1) * (al.index(b) + 1))
