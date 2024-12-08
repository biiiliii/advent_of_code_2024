from utils.solutionBase import SolutionBase
from collections import defaultdict

class solution(SolutionBase):
    data = [list(line.strip()) for line in open("day8/input.txt").readlines()]
    

    def find_anitnode(self, a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        antinode_x = a[0] - dx
        antinode_y = a[1] - dy

        return (antinode_x, antinode_y)

    def find_antinode_line(self, a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        antinode_x = a[0] - dx
        antinode_y = a[1] - dy

        antinodes = set()

        antinodes.add(a)
        
        while 0 <= antinode_x < len(self.data) and 0 <= antinode_y < len(self.data[0]):
            antinodes.add((antinode_x, antinode_y))
            antinode_x -= dx
            antinode_y -= dy

        return antinodes

    def visualize_antinodes(self, antinodes):
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows):
            for j in range(cols):
                if (i, j) in antinodes:
                    print("#", end="")
                else:
                    print(self.data[i][j], end="")
            print()


    def p1(self):
        rows, cols = len(self.data), len(self.data[0])
        antenas = defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                if self.data[i][j] != ".":
                    antenas[self.data[i][j]].append((i, j))

        antinodes = set()
        
        for antena in antenas:
            for px, py in antenas[antena]:
                for p2x, p2y in antenas[antena]:
                    if px != p2x and py != p2y:
                        antinode = self.find_anitnode((px, py), (p2x, p2y))
                        if  0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                            antinodes.add(antinode)
    
        print(len(antinodes))
        
        
                    

    def p2(self):
        rows, cols = len(self.data), len(self.data[0])
        antenas = defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                if self.data[i][j] != ".":
                    antenas[self.data[i][j]].append((i, j))

        antinodes = set()
        
        for antena in antenas:
            for px, py in antenas[antena]:
                for p2x, p2y in antenas[antena]:
                    if px != p2x and py != p2y:
                        antinodes_line = self.find_antinode_line((px, py), (p2x, p2y))
                        for antinode in antinodes_line:
                            if  0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                                antinodes.add(antinode)
    
        print(len(antinodes))
