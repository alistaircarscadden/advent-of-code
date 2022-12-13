from common import *

al = inf_lraw()


nstacks = len(al[0]) // 4
stacks = [[] for _ in range(nstacks)]

for l in al[: indexbykey(al, lambda x: "[" not in x)]:
    for i, g in enumerate(listchunks(l, 4)):
        a = g[1]
        if a != " ":
            stacks[i].insert(0, a)


for l in al:
    if l.startswith("move"):
        a, b, c = map(int, re.findall(r"\d+", l))

        for _ in range(a):
            stacks[c - 1].append(stacks[b - 1].pop())

a = [x.pop() for x in stacks]
print("".join(a))
