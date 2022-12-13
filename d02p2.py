from common import *

al = inf_lstrip()


def toplay(a, b):
    match (a, b):
        case (1, 0):
            return 3
        case (1, 3):
            return 1
        case (1, 6):
            return 2
        case (2, 0):
            return 1
        case (2, 3):
            return 2
        case (2, 6):
            return 3
        case (3, 0):
            return 2
        case (3, 3):
            return 3
        case (3, 6):
            return 1


ts = 0
for l in al:
    a, b = l.split()
    a = convert("ABC", [1, 2, 3], a) or convert("XYZ", [1, 2, 3], a)
    g = convert("XYZ", [0, 3, 6], b)
    score = g + toplay(a, g)
    ts += score

print(ts)
