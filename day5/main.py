page_order = [list(map(int, line.strip().split('|'))) for line in open("input1.txt").readlines()]

page_order_dict = {}

for t in page_order:
    if t[0] not in page_order_dict.keys():
        page_order_dict[t[0]] = [t[1]]
    else:
        page_order_dict[t[0]] += [t[1]]

updates = [list(map(int, line.strip().split(','))) for line in open("input2.txt").readlines()]

def p1():
    global page_order_dict, updates
    result = 0

    for line in updates:
        tmp, tmp2 = [], []
        valid = True
        for i, n in enumerate(line):
            if n in page_order_dict:
                if any(m in page_order_dict[n] for m in tmp):
                    valid = False
                    break
                tmp.append(n)
            tmp2.extend(key for key in page_order_dict if n in page_order_dict[key])
            if any(key in line[i:] for key in tmp2):
                valid = False
                break
        if valid:
            result += line[len(line) // 2]

    print(result)


p1()