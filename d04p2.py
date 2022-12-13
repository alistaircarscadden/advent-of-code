from common import *


s = 0
for l in inf_lstrip():
    a, b = l.split(",")
    x, y = map(int, a.split("-"))
    m, n = map(int, b.split("-"))
    if (
        (x >= m and y <= n)
        or (m >= x and n <= y)
        or (y >= m and n > x)
        or (n >= x and y > m)
    ):
        s += 1

print(s)
