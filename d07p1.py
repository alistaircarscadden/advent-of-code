from common import *

Dir = qdataclass("na co si")
File = qdataclass("na si")

al = inf_lstrip()
toks = (l.split() for l in al)
itr = iternone(toks)
path = []
root = None

while l := next(itr):
    match l:

        case ["$", "cd", ".."]:
            path.pop()

        case ["$", "cd", "/"]:
            root = Dir("/", [], 0)
            path.append(root)

        case ["$", "cd", d]:
            cur = path[-1]
            for c in cur.co:
                if c.na == d:
                    path.append(c)
                    break

        case ["$", "ls"]:
            cur = path[-1]
            while l := next(itr):
                match l:
                    case ["dir", d]:
                        cur.co.append(Dir(d, [], 0))
                    case [s, n]:
                        cur.co.append(File(n, int(s)))
                    case _:
                        itr = itertools.chain([l], itr)
                        break

        case _:
            break


def size(x, w):
    if isinstance(x, Dir):
        si = sum([size(y, w) for y in x.co])
        x.si = si
        if si <= 100000:
            w.append(si)
    return x.si


w = []
size(root, w)
print(sum(w))
