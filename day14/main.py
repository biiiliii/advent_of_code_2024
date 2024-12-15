from utils.solutionBase import SolutionBase
import re

class solution(SolutionBase):
    robots = []
    for line in open("day14/input.txt").readlines():
            robots.append(tuple(map(int, re.findall("-?\d+", line))))



    def p1(self):
        WIDTH = 101
        HEIGHT = 103
        result = []

        for px, py, vx, vy in self.robots:
            result.append(((px + vx * 100)%WIDTH, (py + vy * 100)%HEIGHT))

        tl = bl = tr = br = 0

        VM = (HEIGHT - 1) // 2
        HM = (WIDTH - 1) // 2

        for px, py in result:
            if px == HM or py == VM:
                continue
            if px < HM and py < VM:
                tl += 1
            elif px < HM and py > VM:
                bl += 1
            elif px > HM and py < VM:
                tr += 1
            else:
                br += 1

        return tl * bl * tr * br
    
    