from utils.solutionBase import SolutionBase
import heapq



class solution(SolutionBase):
    data = [list(line.strip()) for line in open("day16/input.txt").readlines()]

    def p1(self):
        rows = len(self.data)
        cols = len(self.data[0])

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "S":
                    sr = r
                    sc = c

        pq = [(0, sr, sc, 0, 1)]
        seen = {(sr, sc, 0, 1)}

        while pq:
            cost, r, c, dr, dc = heapq.heappop(pq)
            seen.add((r, c, dr, dc))
            if self.data[r][c] == "E":
                return cost
            for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
                if self.data[nr][nc] == "#": continue
                if (nr, nc, ndr, ndc) in seen: continue
                heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))
        
    def p2(self):
        rows = len(self.data)
        cols = len(self.data[0])

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "S":
                    sr = r
                    sc = c

        pq = [(0, sr, sc, 0, 1, [])]
        seen = {(sr, sc, 0, 1)}
        
        best_tiles = set()
        best_cost = float("inf")
        while pq:
            cost, r, c, dr, dc, path = heapq.heappop(pq)
            seen.add((r, c, dr, dc))
            path = path + [(r, c)]
            if self.data[r][c] == "E":
                if cost > best_cost: break
                best_cost = cost
                for tile in path:
                    best_tiles.add(tile)
                continue
            for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, -dc, dr), (cost + 1000, r, c, dc, -dr)]:
                if self.data[nr][nc] == "#": continue
                if (nr, nc, ndr, ndc) in seen: continue
                heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc, path))

        for i in range(rows):
            for j in range(cols):
                if (i, j) in best_tiles:
                    print("O", end="")
                else:
                    print(self.data[i][j], end="")
            print()
        return len(best_tiles)
    