from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    data = [line.strip() for line in open("day4/input.txt").readlines()]

    def p1(self):
        f, c = len(self.data), len(self.data[0])
        comptador = 0

        for i in range(f):
            comptador += self.data[i].count("XMAS")
            comptador += self.data[i][::-1].count("XMAS")
        vertical_data = list(map("".join, zip(*self.data)))
        for i in range(f):
            comptador += vertical_data[i].count("XMAS")
            comptador += vertical_data[i][::-1].count("XMAS")

        for i in range(f - 3):
            for j in range(c - 3):
                diagonal = "".join([self.data[i + k][j + k] for k in range(4)])
                comptador += diagonal.count("XMAS")
                comptador += diagonal[::-1].count("XMAS")
        for i in range(3, f):
            for j in range(c - 3):
                diagonal = "".join([self.data[i - k][j + k] for k in range(4)])
                comptador += diagonal.count("XMAS")
                comptador += diagonal[::-1].count("XMAS")
        return comptador

    def p2(self):
        f, c = len(self.data), len(self.data[0])
        comptador = 0

        for i in range(1, f - 1):
            for j in range(1, c - 1):
                if self.data[i][j] == 'A':
                    diagonal_right = "".join([self.data[i + k][j + k] for k in range(-1, 2)])
                    diagonal_left = "".join([self.data[i - k][j + k] for k in range(-1, 2)])
                    if (diagonal_left.count("MAS") + diagonal_left[::-1].count("MAS")) and (diagonal_right.count("MAS") + diagonal_right[::-1].count("MAS")):
                        comptador += 1

        return comptador
