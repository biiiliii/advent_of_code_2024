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
        valid = True
        for i, n in enumerate(line):
            if n in page_order_dict:
                if any(m in page_order_dict[n] for m in line[:i]):
                    valid = False
                    break
        if valid:
            result += line[len(line) // 2]

    print(result)


def p2():
    global page_order_dict, updates
    
    result = 0
    for line in updates:
        valid = True
        for i, n in enumerate(line):
            if n in page_order_dict:
                if any(m in page_order_dict[n] for m in line[:i]):
                    valid = False
                    break
        if not valid:
            filter = {i: set(page_order_dict[i]) & set(line) for i in line if i in page_order_dict}        
            result += sorted(filter, key=lambda k: len(filter[k]), reverse=True)[len(line) // 2]
    
    print(result)

p1()