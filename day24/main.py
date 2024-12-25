from utils.solutionBase import SolutionBase

class solution(SolutionBase):
    initial, loop = open("day24/input.txt").read().split("\n\n")
    debug = False

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
        

    def pp(self, wire, keys, depth=0):
        if wire[0] in "xy": return "  " * depth + wire
        op, x, y, = keys[wire]
        return "  " * depth + op + " (" + wire + ")\n" + self.pp(x, keys, depth + 1) + "\n" + self.pp(y, keys, depth + 1)

    def make_wire(self, char, num):
        return char + str(num).rjust(2, "0")

    def verify_z(self, wire, num):
        if self.debug:
            print("vz", wire, num)
        if wire not in self.keys: return False
        op, x, y = self.keys[wire]
        if op != "XOR": return False
        if num == 0: return sorted([x, y]) == ["x00", "y00"]
        return self.verify_intermediate_xor(x, num) and self.verify_carry_bit(y, num) or self.verify_intermediate_xor(y, num) and self.verify_carry_bit(x, num)

    def verify_intermediate_xor(self, wire, num):
        if self.debug:
            print("vx", wire, num)
        if wire not in self.keys: return False
        op, x, y = self.keys[wire]
        if op != "XOR": return False
        return sorted([x, y]) == [self.make_wire("x", num), self.make_wire("y", num)]

    def verify_carry_bit(self, wire, num):
        if self.debug:
            print("vc", wire, num)
        if wire not in self.keys: return False
        op, x, y = self.keys[wire]
        if num == 1:
            if op != "AND": return False
            return sorted([x, y]) == ["x00", "y00"]
        if op != "OR": return False
        return self.verify_direct_carry(x, num - 1) and self.verify_recarry(y, num - 1) or self.verify_direct_carry(y, num - 1) and self.verify_recarry(x, num - 1)


    def verify_direct_carry(self, wire, num):
        if self.debug:
            print("vd", wire, num)
        if wire not in self.keys: return False
        op, x, y = self.keys[wire]
        if op != "AND": return False
        return sorted([x, y]) == [self.make_wire("x", num), self.make_wire("y", num)]

    def verify_recarry(self, wire, num):
        if self.debug:
            print("vr", wire, num)
        if wire not in self.keys: return False
        op, x, y = self.keys[wire]
        if op != "AND": return False
        return self.verify_intermediate_xor(x, num) and self.verify_carry_bit(y, num) or self.verify_intermediate_xor(y, num) and self.verify_carry_bit(x, num)

    def verify(self, num):
        return self.verify_z(self.make_wire("z", num), num)
    
    def progress(self):
        i = 0
        while True:
            if not self.verify(i):
                return i
            i += 1

    def p2(self):
        self.keys = {}
        for key in self.loop.splitlines():
            splited_key = key.split(" ")
            self.keys[splited_key[4]] = (splited_key[1], splited_key[0], splited_key[2])
        
        # self.debug = True
        swaps = []
        for _ in range(4):
            baseline = self.progress()
            for x in self.keys:
                for y in self.keys:
                    if x == y: continue
                    self.keys[x], self.keys[y] = self.keys[y], self.keys[x]
                    if self.progress() > baseline:
                        break
                    self.keys[x], self.keys[y] = self.keys[y], self.keys[x]
                else:
                    continue
                break
            swaps.extend([x, y])
                    
        return ",".join(sorted(swaps))
        
        