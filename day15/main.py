from utils.solutionBase import SolutionBase
import time
import os

class solution(SolutionBase):
    data = open("day15/input.txt").read()

    def move_to_dir(self, pos, direction, _map):
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        if _map[new_pos[1]][new_pos[0]] == "#":
            return pos, _map
        
        if _map[new_pos[1]][new_pos[0]] == "O":
            next_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            while _map[next_pos[1]][next_pos[0]] == "O":
                next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
            if _map[next_pos[1]][next_pos[0]] == ".":
                _map[next_pos[1]][next_pos[0]] = "O"
                _map[new_pos[1]][new_pos[0]] = "@"
                _map[pos[1]][pos[0]] = "."
                return new_pos, _map
            else:
                return pos, _map
        
        if _map[new_pos[1]][new_pos[0]] == ".":
            _map[new_pos[1]][new_pos[0]] = "@"
            _map[pos[1]][pos[0]] = "."
            return new_pos, _map
        
        return pos, _map

    def p1(self):
        _map, _commands = self.data.split("\n\n")
        _map = [list(line) for line in _map.split("\n")]
        for i in range(len(_map)):
            for j in range(len(_map[i])):
                if _map[i][j] == "@":
                    pos = (j, i)
                    break
        
        possible_commands = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        for command in _commands:
            if command == "\n": continue
            new_dir = possible_commands[command]
            pos, _map = self.move_to_dir(pos, new_dir, _map)
            """os.system("cls")
            print("MOVING TO ", command)
            for i in range(len(_map)):
                print("".join(_map[i]))"""

        return sum(100 * i + j for i in range(len(_map)) for j in range(len(_map[i])) if _map[i][j] == "O")

    def p2(self):
        _map, _commands = self.data.split("\n\n")

        expansion = {"#": "##", ".": "..", "O": "[]", "@": "@."}
        _map = [list("".join([expansion[char] for char in line])) for line in _map.splitlines()]


        for i in range(len(_map)):
            for j in range(len(_map[i])):
                if _map[i][j] == "@":
                    x, y = (j, i)
                    break
                    
        
        possible_commands = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

        for command in _commands:
            if command == "\n": continue
            dx, dy = possible_commands[command]
            targets = [(x, y)]
            go = True
            for cx, cy in targets:
                nx = cx + dx
                ny = cy + dy
                if (nx, ny) in targets: continue
                char = _map[ny][nx]
                if char == "#":
                    go = False
                    break
                if char == "[":
                    targets.append((nx, ny))
                    targets.append((nx + 1, ny))
                if char == "]":
                    targets.append((nx, ny))
                    targets.append((nx - 1, ny))

            if not go: continue
            copy = [list(line) for line in _map]

            _map[y][x] = "."
            _map[y + dy][x + dx] = "@"

            for bx, by in targets[1:]:
                _map[by][bx] = "."
            for bx, by in targets[1:]:
                _map[by + dy][bx + dx] = copy[by][bx]

            x += dx
            y += dy

            """os.system("cls")
            print("MOVING TO ", command)
            for i in range(len(_map)):
                print("".join(_map[i]))"""

        return sum(100 * i + j for i in range(len(_map)) for j in range(len(_map[i])) if _map[i][j] == "[")