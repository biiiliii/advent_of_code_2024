from utils.solutionBase import SolutionBase
import copy

class solution(SolutionBase):
    data = [[int(n) if n in "1234567890" else -1 for n in line.strip()] for line in open("day10/input.txt")]

    def backtrack(self, y, x, val, visited, delete_top=True):
        if val == 9:
            self.data[y][x] = -1 if delete_top else self.data[y][x]
            return 1
        paths = 0
        visited.add((y, x))
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(self.data) and 0 <= nx < len(self.data[0]) and (ny, nx) not in visited:
                if self.data[ny][nx] == val + 1:
                    paths += self.backtrack(ny, nx, val + 1, visited, delete_top)
        visited.remove((y, x))
        return paths

    def p1(self):

        trailheads = list()
        for y, i in enumerate(self.data):
            for x, j in enumerate(i):
                if j == 0:
                    trailheads.append((y, x))
        result = 0
        _idx = 0
        backup = copy.deepcopy(self.data)
        while _idx < len(trailheads):
            y, x = trailheads[_idx]
            self.data = copy.deepcopy(backup)
            result += self.backtrack(y, x, 0, set()) 
            _idx += 1
        return result


    def p2(self):
        trailheads = list()
        for y, i in enumerate(self.data):
            for x, j in enumerate(i):
                if j == 0:
                    trailheads.append((y, x))
        
        result = 0
        _idx = 0
        while _idx < len(trailheads):
            y, x = trailheads[_idx]
            result += self.backtrack(y, x, 0, set(), False) 
            _idx += 1
        return result