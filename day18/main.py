from utils.solutionBase import SolutionBase
from collections import deque



class solution(SolutionBase):
    data = [tuple(map(int, line.split(","))) for line in open("day18/input.txt")]

    def p1(self):
        size = 70

        corrupted = self.data[:1024]
        q = deque([(0, 0, 0)])
        visited = {(0, 0)}

        while q:
            cx, cy, d = q.popleft()
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                if (nx, ny) in visited: continue
                if nx < 0 or nx > size or ny < 0 or ny > size: continue
                if (nx, ny) in corrupted: continue
                if (nx, ny) == (size, size): return d+1
                visited.add((nx, ny))
                q.append((nx, ny, d + 1))

    def p2(self):
        size = 70

        for i in range(len(self.data), 0, -1):
            corrupted = self.data[:i]
            q = deque([(0, 0)])
            visited = {(0, 0)}

            while q:
                cx, cy = q.popleft()
                for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                    if (nx, ny) in visited: continue
                    if nx < 0 or nx > size or ny < 0 or ny > size: continue
                    if (nx, ny) in corrupted: continue
                    if (nx, ny) == (size, size): return self.data[i]
                    visited.add((nx, ny))
                    q.append((nx, ny))