from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    initial, loop = open("day24/input.txt").read().split("\n\n")

    def p1(self):
        vals = {}
        for line in self.initial.splitlines():
            splited_line = line.split(": ")
            vals[splited_line[0]] = int(splited_line[1])

        keys = set()
        for key in self.loop.splitlines():
            splited_key = key.split(" ")
            keys.add(splited_key[0])
            keys.add(splited_key[2])
            keys.add(splited_key[4])
        
        while len(vals.keys()) < len(keys):
            for key in self.loop.splitlines():
                splited_key = key.split(" ")
                v1, v2, v3 = splited_key[0], splited_key[2], splited_key[4]
                op = splited_key[1]
                if any(v not in vals.keys() for v in [v1, v2]): continue
                match op:
                    case "AND":
                        vals[v3] = vals[v1] and vals[v2]
                    case "OR":
                        vals[v3] = vals[v1] or vals[v2]
                    case "XOR":
                        vals[v3] = vals[v1] ^ vals[v2]
        
        bin_val = "".join([str(vals[key]) if key[0] == "z" else "" for key in sorted(list(keys), reverse=True)])
        return int(bin_val, 2)
            