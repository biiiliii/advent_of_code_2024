from utils.solutionBase import SolutionBase
from collections import deque
from itertools import product
from functools import cache

num_keyboard = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

dir_keyboard = [
    [None, "^", "A"],
    ["<", "v", ">"]
]


class solution(SolutionBase):
    data = [line.strip() for line in open("day21/input.txt").readlines()]

    def pathfind(self, keyboard, start, end):

        for r in range(len(keyboard)):
            for c in range(len(keyboard[r])):
                if keyboard[r][c] == start:
                    s = (r, c)
                if keyboard[r][c] == end:
                    e = (r, c)
        
        q = deque([(s[0], s[1], "")])
        # visited = set()
        # visited.add((s[0], s[1]))

        pos_keys = {
            (0, -1) : "<",
            (0, 1) : ">",
            (-1, 0): "^",
            (1, 0) : "v"
        }

        optimal = float("inf")
        possibilities = []
        while q:
            cr, cc, path = q.popleft()
            
            for nr, nc in [(cr, cc+1), (cr, cc-1), (cr+1, cc),  (cr-1, cc)]:
                if nr < 0 or nc < 0 or nr >= len(keyboard) or nc >= len(keyboard[0]): continue
                # if (nr, nc) in visited: continue
                if keyboard[nr][nc] is None: continue
                key = pos_keys[(nr - cr, nc - cc)]
                if (nr, nc) == e:
                    if optimal < len(path) + 1: break
                    optimal = len(path) + 1
                    possibilities.append(path+key+"A")
                else:
                    q.append((nr, nc, path + key))
                    #visited.add((nr, nc))
            else:
                continue
            break
        return possibilities

    def get_seqs(self, keyboard):
        pos = {}
        for r in range(len(keyboard)):
            for c in range(len(keyboard[r])):
                if keyboard[r][c] is not None: pos[keyboard[r][c]] = (r, c)
        

        seqs = {}
        for x in pos:
            for y in pos:
                if x == y:
                    seqs[(x, y)] = ["A"]
                    continue
                seqs[(x, y)] = self.pathfind(keyboard, x, y)
        return seqs

    def solver(self, keyboard, string):
        seqs = self.get_seqs(keyboard)
        

        options = [seqs[x, y] for x, y in zip("A" + string, string)]
        return ["".join(x) for x in product(*options)]



    """
    # This is the code I used for the first part of the problem and takes a couple of seconds to run
    # But since I had to optimize it for the second part, I also created the faster version of p1
    
    def p1(self):
        result = 0
        for i in range(len(self.data)):
            next = self.solver(num_keyboard, self.data[i])
            for _ in range(2):
                possible_next = []
                for sol in next:
                    possible_next.extend(self.solver(dir_keyboard, sol))
                minlen = min(map(len, possible_next))
                next = [sol for sol in possible_next if len(sol) == minlen]

            int_of_string = int("".join([x for x in self.data[i] if x.isdigit()]))
            result += int_of_string * len(next[0])
        return result
        
        
        """
    def p1(self):
        self.dir_seqs = self.get_seqs(dir_keyboard)
        self.num_seqs = self.get_seqs(num_keyboard)
        self.len_dir_seqs = {k: len(v[0]) for k, v in self.dir_seqs.items()}
        
        result = 0
        
        for line in self.data:
            inputs = self.solver(num_keyboard, line)
            length = min(self.depth_check(subseq, 2) for subseq in inputs)
            int_of_string = int("".join([x for x in line if x.isdigit()]))
            result += int_of_string * length

        return result

    @cache
    def depth_check(self, seq, depth=25):
        if depth == 1: return sum(self.len_dir_seqs[(x, y)] for x, y in zip("A" + seq, seq))
        length = 0
        for x, y in zip("A" + seq, seq):
            length += min(self.depth_check(subseq, depth-1) for subseq in self.dir_seqs[(x, y)])
        return length
    

    def p2(self):
        self.dir_seqs = self.get_seqs(dir_keyboard)
        self.num_seqs = self.get_seqs(num_keyboard)
        self.len_dir_seqs = {k: len(v[0]) for k, v in self.dir_seqs.items()}

        
        result = 0
        
        for line in self.data:
            inputs = self.solver(num_keyboard, line)
            length = min(map(self.depth_check, inputs))
            int_of_string = int("".join([x for x in line if x.isdigit()]))
            result += int_of_string * length

        return result
