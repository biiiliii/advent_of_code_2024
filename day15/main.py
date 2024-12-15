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
                    
        
        possible_commands = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        for command in _commands:
            if command == "\n": continue
            new_dir = possible_commands[command]
            pos, _map = self.move_to_dir(pos, new_dir, _map)
            """os.system("cls")
            print("MOVING TO ", command)
            for i in range(len(_map)):
                print("".join(_map[i]))"""

        result = 0
        for i in range(len(_map)):
            for j in range(len(_map[i])):
                if _map[i][j] == "O":
                    result += 100*i + j
        return result