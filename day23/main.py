from utils.solutionBase import SolutionBase
from collections import defaultdict
from itertools import permutations


class solution(SolutionBase):
    data = [line.strip() for line in open("day23/input.txt")]

    def p1(self):
        computer_connections = defaultdict(list)
        for line in self.data:
            c1, c2 = line.split("-")
            if c2 not in computer_connections[c1]: computer_connections[c1].append(c2)
            if c1 not in computer_connections[c2]: computer_connections[c2].append(c1)
            
        c = 0
        counted_connections = set()
        for c1 in computer_connections:
            for c2 in computer_connections[c1]:
                for c3 in computer_connections[c2]:
                    if c3 in computer_connections[c1]:
                        if tuple(sorted([c1, c2, c3])) in counted_connections: continue
                        if (c1.startswith("t") or c2.startswith("t") or c3.startswith("t")):
                            counted_connections.add(tuple(sorted((c1, c2, c3))))
                            c += 1
        
        return c
    

    def search_conns(self, node, _set):
        key = tuple(sorted(_set))
        if key in self.sets: return
        self.sets.add(key)
        for conn in self.comp_cons[node]:
            if conn in _set: continue
            if not all(conn in self.comp_cons[c] for c in _set): continue
            _set.add(conn)
            self.search_conns(conn, {*_set, conn}) 
    
    def p2(self):
        computer_connections = defaultdict(list)
        for line in self.data:
            c1, c2 = line.split("-")
            if c2 not in computer_connections[c1]: computer_connections[c1].append(c2)
            if c1 not in computer_connections[c2]: computer_connections[c2].append(c1)
        
        self.comp_cons = computer_connections
        self.sets = set()
        for conn in computer_connections:
            self.search_conns(conn, {conn})

        return ",".join(max(self.sets, key=len))
