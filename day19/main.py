from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    patterns, desings = open("day19/input.txt").read().split("\n\n")


    def possible(self, patterns, design):
        if design == "": return True
        for pattern in patterns:
            if design.startswith(pattern):
                if self.possible(patterns, design[len(pattern):]):
                    return True
        return False


    def p1(self):
        p = [t.strip() for t in self.patterns.split(",")]
        d = [line for line in self.desings.split("\n")]


        c = 0
        for i in range(len(d)):
            if self.possible(p, d[i]):
                c += 1
        return c