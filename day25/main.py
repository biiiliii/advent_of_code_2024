from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    data = open("day25/input.txt").read().split("\n\n")

    def p1(self):
        keys = []
        locks = []
        for block in self.data:
            tmp = [0]*5
            for line in block.splitlines()[1:-1]:
                tmp = [x+y for x,y in zip(tmp, [1 if c == "#" else 0 for c in line])]
            if "#" in block[0]: locks.append(tmp)
            else: keys.append(tmp)
        
        c = 0
        for lock in locks:
            for key in keys:
                if any(x + y >= 6 for x, y in zip(lock, key)): continue
                c += 1
        return c