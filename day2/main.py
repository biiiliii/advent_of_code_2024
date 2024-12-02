data = [list(map(int, line.split())) for line in open("input.txt").readlines()]

def p1():
    safe_count = 0
    for lst in data:
        if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
            if all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:])):
                safe_count += 1
    print(safe_count)


p1()
