with open("input") as f:
    totals = []
    cur_total = 0

    for line in f.readlines():
        line = line.strip()
        if line == "":
            totals.append(cur_total)
            cur_total = 0
        else:
            cur_total += int(line)

    if cur_total > 0:
        totals.append(cur_total)

    totals.sort()
    print(sum(totals[-3:]))
