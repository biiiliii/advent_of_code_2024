from utils.solutionBase import SolutionBase
from collections import deque


MIN_CHEAT = 50

class solution(SolutionBase):
    data = [line.strip() for line in open("day20/input.txt").readlines()]


    """
    # I used this code for the first part of the problem, but it is not efficient enough for the second part
    # So when making the second part, I realized that I could change the code and make it faster
    
    def cheat(self, path, idx):
        pos = path[idx]
        dirs_can_cheat = 0
        for pcheat in path[idx + 2:]:
            if (abs(pos[0] - pcheat[0]) == 2 and pos[1] == pcheat[1]) or (abs(pos[1] - pcheat[1]) == 2 and pos[0] == pcheat[0]):
                if abs(path.index(pcheat) - path.index(pos)) - 1 > MIN_CHEAT:
                    dirs_can_cheat += 1
        return dirs_can_cheat

    def p1(self):
        rows = len(self.data)
        cols = len(self.data[0])

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "S":
                    start = (r, c)
                    break
        
        q = deque([(start[0], start[1], [])])
        visited = set()
        visited.add((start[0], start[1]))
        while q:
            cr, cc, path = q.popleft()
            if self.data[cr][cc] == "E":
                break
            for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if (nr, nc) in visited: continue
                if self.data[nr][nc] == "#": continue
                q.append((nr, nc, path + [(nr, nc)]))
                visited.add((nr, nc))

        return sum(self.cheat(path, i) for i in range(len(path)))
        
        
        """
    
    def p1(self):
        rows = len(self.data)
        cols = len(self.data[0])

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "S":
                    start = (r, c)
    
        
        grid = [[-1] * cols for _ in range(rows)]
        grid[start[0]][start[1]] = 0
        q = deque([(start[0], start[1])])

        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if grid[nr][nc] != -1: continue
                if self.data[nr][nc] == "#": continue
                grid[nr][nc] = grid[cr][cc] + 1
                q.append((nr, nc))

        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1: continue
                for dr in range(3):
                    dc = 2 - dr
                    for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                        if grid[nr][nc] == -1: continue
                        if grid[r][c] - grid[nr][nc] >= 100 + 2: count += 1
        return count

    def p2(self):
        rows = len(self.data)
        cols = len(self.data[0])

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "S":
                    start = (r, c)
                    
        
        grid = [[-1] * cols for _ in range(rows)]
        grid[start[0]][start[1]] = 0
        q = deque([(start[0], start[1])])

        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if grid[nr][nc] != -1: continue
                if self.data[nr][nc] == "#": continue
                grid[nr][nc] = grid[cr][cc] + 1
                q.append((nr, nc))

        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1: continue
                for radius in range(2, 21):
                    for dr in range(radius + 1):
                        dc = radius - dr
                        for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                            if grid[nr][nc] == -1: continue
                            if grid[r][c] - grid[nr][nc] >= 100 + radius: count += 1
        return count