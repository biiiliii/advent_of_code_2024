data = [list(map(int, line.split())) for line in open("input.txt").readlines()]

def p1():
    safe_count = 0
    for lst in data:
        if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
            if all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:])):
                safe_count += 1 
    print(safe_count)

def p2():
    safe_count = 0
    for lst in data:
        if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
            if all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:])):
                safe_count += 1
            else:
                for i in range(len(lst)):
                    new_lst = lst.copy()
                    del new_lst[i]
                    if sorted(new_lst) == new_lst or sorted(new_lst, reverse=True) == new_lst:
                        if all(1 <= abs(a - b) <= 3 for a, b in zip(new_lst, new_lst[1:])):
                            safe_count += 1
                            break
        else:
            for i in range(len(lst)):
                new_lst = lst.copy()
                del new_lst[i]
                if sorted(new_lst) == new_lst or sorted(new_lst, reverse=True) == new_lst:
                    if all(1 <= abs(a - b) <= 3 for a, b in zip(new_lst, new_lst[1:])):
                        safe_count += 1
                        break
    print(safe_count)


p2()
