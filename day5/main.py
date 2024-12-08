from utils.solutionBase import SolutionBase

class solution(SolutionBase):

    page_order_dict = {}
    updates = []

    
    page_order = [list(map(int, line.strip().split('|'))) for line in open("day5/input1.txt").readlines()]
    for t in page_order:
        if t[0] not in page_order_dict:
            page_order_dict[t[0]] = [t[1]]
        else:
            page_order_dict[t[0]] += [t[1]]

    updates = [list(map(int, line.strip().split(','))) for line in open("day5/input2.txt").readlines()]

    def p1(self):
        result = 0
        for line in self.updates:
            valid = True
            for i, n in enumerate(line):
                if n in self.page_order_dict:
                    if any(m in self.page_order_dict[n] for m in line[:i]):
                        valid = False
                        break
            if valid:
                result += line[len(line) // 2]
        return result

    def p2(self):
        result = 0
        for line in self.updates:
            valid = True
            for i, n in enumerate(line):
                if n in self.page_order_dict:
                    if any(m in self.page_order_dict[n] for m in line[:i]):
                        valid = False
                        break
            if not valid:
                filter = {i: set(self.page_order_dict[i]) & set(line) for i in line}
                result += sorted(filter, key=lambda k: len(filter[k]), reverse=True)[len(line) // 2]
        return result

