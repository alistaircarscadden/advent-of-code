from common import *

al = [l.split("->") for l in inf_lstrip()]
al = [[list(map(int, x.strip().split(","))) for x in l] for l in al]
left = 0
right = 0
bottom = 0
for l in al:
    for c in l:
        left = min(c[0], left)
        right = max(c[0], right)
        bottom = max(c[1], bottom)

grid = [["." for _ in range(right + 150)] for _ in range(bottom + 5)]

for l in al:
    for a, b in itertools.pairwise(l):
        c1, r1 = a
        c2, r2 = b

        if c1 < c2:
            for x in range(c1, c2 + 1):
                grid[r1][x] = "#"
        if c1 > c2:
            for x in range(c2, c1 + 1):
                grid[r1][x] = "#"
        if r1 < r2:
            for x in range(r1, r2 + 1):
                grid[x][c1] = "#"
        if r1 > r2:
            for x in range(r2, r1 + 1):
                grid[x][c1] = "#"


over = False
sand = 0
bottom = bottom + 1
while not over:
    r, c = 0, 500
    rest = False

    while not rest and not over:
        if r == bottom:
            rest = True
            grid[r][c] = "o"
            sand += 1
            if r == 0 and c == 500:
                over = True
        elif grid[r + 1][c] == ".":
            r = r + 1
        elif grid[r + 1][c - 1] == ".":
            r, c = r + 1, c - 1
        elif grid[r + 1][c + 1] == ".":
            r, c = r + 1, c + 1
        else:
            rest = True
            grid[r][c] = "o"
            sand += 1
            if r == 0 and c == 500:
                over = True

# used this to visualize my bugs:
# for l in grid:
#     for c in l:
#         print(end=c)
#     print()

# it drew this for me (same as example except my bottom floor is made of magic instead of #s):
# ................o................
# ...............ooo...............
# ..............ooooo..............
# .............ooooooo.............
# ............oo#ooo##o............
# ...........ooo#ooo#ooo...........
# ..........oo###ooo#oooo..........
# .........oooo.oooo#ooooo.........
# ........oooooooooo#oooooo........
# .......ooo#########ooooooo.......
# ......ooooo.......ooooooooo......
# .................................

print(sand)
