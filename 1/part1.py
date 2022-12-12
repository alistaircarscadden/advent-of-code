with open("input") as f:
    best_total = 0
    cur_total = 0

    for line in f.readlines():
        line = line.strip()
        if line == "":
            print(f" = {cur_total}")
            best_total = max(best_total, cur_total)
            cur_total = 0
        else:
            print(end=f"+{line}")
            cur_total += int(line)

    if cur_total > 0:
        print(f" = {cur_total}")
        best_total = max(best_total, cur_total)

    print(f"best = {best_total}")
