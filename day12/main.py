from utils.solutionBase import SolutionBase
from collections import deque

class solution(SolutionBase):
    data = [list(line.strip()) for line in open("day12/input.txt").readlines()]

    def perimeter(self, region):
        result = 0
        for r, c in region:
            result += 4
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (nr, nc) in region:
                    result -= 1
        return result

    def p1(self):
        rows = len(self.data)
        cols = len(self.data[0])

        regions = list()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen: continue
                seen.add((r, c))
                region = {(r, c)}
                q = deque([(r, c)])
                crop = self.data[r][c]
                while q:
                    cr, cc = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dx, cc + dy
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                        if self.data[nr][nc] != crop: continue
                        if (nr, nc) in region: continue
                        region.add((nr, nc))
                        q.append((nr, nc))
                seen |= region
                regions.append(region)

        return sum(len(region) * self.perimeter(region) for region in regions)
    
    def corners(self, region):
        corner_candidates = set()
        for r, c in region:
            for cr, cc in [(r-0.5, c-0.5), (r+0.5, c-0.5), (r+0.5, c+0.5), (r-0.5, c+0.5)]:
                corner_candidates.add((cr, cc))
        corners = 0
        for cr, cc in corner_candidates:
            config = [(sr, sc) in region for sr, sc in [(cr-0.5, cc-0.5), (cr+0.5, cc-0.5), (cr+0.5, cc+0.5), (cr-0.5, cc+0.5)]]
            number = sum(config)
            if number == 1 or number == 3:
                corners += 1
            elif config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        return corners
                
    def p2(self):
        rows = len(self.data)
        cols = len(self.data[0])

        regions = list()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen: continue
                seen.add((r, c))
                region = {(r, c)}
                q = deque([(r, c)])
                crop = self.data[r][c]
                while q:
                    cr, cc = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dx, cc + dy
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                        if self.data[nr][nc] != crop: continue
                        if (nr, nc) in region: continue
                        region.add((nr, nc))
                        q.append((nr, nc))
                seen |= region
                regions.append(region)

        return sum(len(region) * self.corners(region) for region in regions)