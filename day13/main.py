from utils.solutionBase import SolutionBase
import re
from sympy import symbols, Eq, solve



class solution(SolutionBase):
    not_parsed_data = [line for line in open("day13/input.txt").read().split("\n\n")]

    def p1(self):
        data = []
        for line in self.not_parsed_data:
            data.append(list(map(int, re.findall(r"\d+", line))))

        result = 0
        
        for ax, ay, bx, by, px, py in data:
            minimum = float("inf")
            for i in range(101):
               for j in range(101):
                   if ax * i + bx * j == px and ay * i + by * j == py:
                       if i + j < minimum:
                           minimum = min(minimum, i*3 + j)
            if minimum != float("inf"):
                result += minimum
        return result
    
    def p2(self):
        data = []
        for line in self.not_parsed_data:
            data.append(list(map(int, re.findall(r"\d+", line))))

        result = 0
        for ax, ay, bx, by, px, py in data:
            px += 10000000000000
            py += 10000000000000
            x, y = symbols('x y')
            eq1 = Eq(ax * x + bx * y, px)
            eq2 = Eq(ay * x + by * y, py)
            sol = solve((eq1, eq2), (x, y))
            if sol[x] % 1 == 0 and sol[y] % 1 == 0:
                result += sol[x] * 3 + sol[y]
        return result