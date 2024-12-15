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
    

    """
    DISCLAIMER:
    I don't know if this solves the problem for all cases, but it worked for me.

    Instead of trying to find the image, i just checked if, at some points, no robots were in the same position.
    """
    def p2(self):
        WIDTH = 101
        HEIGHT = 103

        for second in range(WIDTH * HEIGHT):
            result = []
            for px, py, vx, vy in self.robots:
                result.append(((px + vx * second)%WIDTH, (py + vy * second)%HEIGHT))
            if len(set(result)) == len(result):
                
                """for i in range(HEIGHT):
                    for j in range(WIDTH):
                        if (j, i) in result:
                            print("#", end="")
                        else:
                            print(".", end="")
                    print()"""
                
                return second
        
