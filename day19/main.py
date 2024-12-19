from utils.solutionBase import SolutionBase
from functools import cache

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

        return sum(1 if self.possible(p, design) else 0 for design in d)
    
    @cache
    def possibilities(self, design, patterns):
        if design == "": return 1
        c = 0
        for pattern in patterns:
            if design.startswith(pattern):
                c += self.possibilities(design[len(pattern):], patterns)
        return c

    def p2(self):
        p = tuple(t.strip() for t in self.patterns.split(","))
        d = [line for line in self.desings.split("\n")]
        
        return sum(self.possibilities(design, p) for design in d)