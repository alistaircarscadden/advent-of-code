from common import *

Node = qdataclass("el ed md")  # elevation edges min_distance_to_reach

al = inf_lstrip()

# create grid of nodes with elation and empty ed listelation
grid = []
snode = None
enode = None
for l in al:
    row = []
    for c in l:
        if c == "S":
            n = Node(ord("a"), [], 0)
            snode = n
        elif c == "E":
            n = Node(ord("z"), [], 10e10)
            enode = n
        else:
            n = Node(ord(c), [], 10e10)
        row.append(n)
    grid.append(row)

rowmax = len(grid)
colmax = len(grid[0])

# fill each nodes ed list
for r in range(rowmax):
    for c in range(colmax):
        cur = grid[r][c]

        if c - 1 >= 0:
            oth = grid[r][c - 1]
            if cur.el >= oth.el - 1:
                cur.ed.append(oth)
        if r - 1 >= 0:
            oth = grid[r - 1][c]
            if cur.el >= oth.el - 1:
                cur.ed.append(oth)
        if c + 1 < colmax:
            oth = grid[r][c + 1]
            if cur.el >= oth.el - 1:
                cur.ed.append(oth)
        if r + 1 < rowmax:
            oth = grid[r + 1][c]
            if cur.el >= oth.el - 1:
                cur.ed.append(oth)

q = []

# part2: now make all "a" have min_distance 0 and push them all to the queue
for r in range(rowmax):
    for c in range(colmax):
        node = grid[r][c]
        if node.el == ord("a"):
            node.md = 0
            q.append(node)

# solve shortest path

while q:
    node = q.pop()
    for oth in node.ed:
        stepsoth = node.md + 1
        if oth.md > stepsoth:
            oth.md = stepsoth
            q.append(oth)

print(enode.md)
