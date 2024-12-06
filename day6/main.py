from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    data_backup = [line.strip() for line in open("day6/input.txt").readlines()]

    def get_guard_position(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] not in ['#', '.', 'X']:
                    return (i, j)

    def count_visited(self):
        count = 0
        for i in range(len(self.data)):
            count += self.data[i].count('X')
        return count
    
    def patrol(self, map, pos=None, idx=None):
        if not pos:
            pos = self.get_guard_position()

        if not idx:
            idx = 0

        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        rows, cols = len(map), len(map[0])

        visited = set()
        visited.add((pos[0], pos[1]))

        visited_entry = {}

        while True:
            d = dirs[idx]
            n = (pos[0] + d[0], pos[1] + d[1])

            if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
                return True, visited, visited_entry 

            if map[n[0]][n[1]] == "#":
                idx = (idx + 1) % 4
                continue
            else:
                visited.add((n[0], n[1]))
                if n not in visited_entry:
                    visited_entry[n] = (pos, idx)
                elif visited_entry[n] == (pos, idx):
                    return False, None, None
                pos = n

    def p1(self):
        self.data = self.data_backup.copy()
        print(len(self.patrol(self.data)[1]))

    def p2(self):
        map = [list(row) for row in self.data_backup]
        _, visited, visited_entry = self.patrol(map)

        visited.remove(self.get_guard_position())
        count = 0

        for vi, vj in visited:
            copy = [row[:] for row in map]
            copy[vi][vj] = "#"

            pos = visited_entry[(vi, vj)][0]
            idx = visited_entry[(vi, vj)][1]

            if not self.patrol(copy, pos, idx)[0]:
                count += 1

        print(count)
