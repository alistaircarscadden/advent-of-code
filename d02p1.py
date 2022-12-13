from common import *

al = inf_lstrip()


def score(a, b):
    match (a, b):
        case (1, 1):
            return 3
        case (1, 2):
            return 0
        case (1, 3):
            return 6
        case (2, 1):
            return 6
        case (2, 2):
            return 3
        case (2, 3):
            return 0
        case (3, 1):
            return 0
        case (3, 2):
            return 6
        case (3, 3):
            return 3


ts = 0
for l in al:
    a, b = l.split()
    rps = lambda x: convert("ABC", [1, 2, 3], x) or convert("XYZ", [1, 2, 3], x)
    a = rps(a)
    b = rps(b)
    s = b + score(b, a)
    ts += s

print(ts)
