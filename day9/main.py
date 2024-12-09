from utils.solutionBase import SolutionBase

class solution(SolutionBase):

    data = list(map(int, open("day9/input.txt").read().strip()))

    def set_free_space(self):
        is_free_space = False
        _set = list()
        _idx = 0
        for num in self.data:
            for _ in range(num):
                _set.append("." if is_free_space else str(_idx))
            _idx += 1 if is_free_space else 0
            is_free_space = not is_free_space
        return _set

    def p1(self):
        line = self.set_free_space()
        left = 0
        right = len(line) - 1
        while left < right:
            if line[left] == "." and line[right] != ".":
                line[left], line[right] = line[right], line[left]
                left += 1
                right -= 1
            elif line[left] != ".":
                left += 1
            elif line[right] == ".":
                right -= 1
        
        result = 0
        for x, num in enumerate(line[:right+1]):
            if num != ".":
                result += x * int(num)
        
        return result

    def find_point_pack(self, line, length, max_idx):
        idx = 0
        while idx < max_idx:
            if line[idx] == ".":
                count = 0
                while line[idx + count] == ".":
                    count += 1
                    if count == length:
                        return idx
                idx += count
            idx += 1
        return -1
    
    def p2(self):
        line:int = self.set_free_space()
        right:int = len(line) - 1
        right_len:int = 0
        while right >= 0:
            if line[right] != ".":
                _char = line[right]
                while line[right + right_len] == _char:
                    right_len -= 1
                _idx = self.find_point_pack(line, abs(right_len), right)
                if _idx != -1:
                    while right_len < 0:
                        line[_idx] = _char
                        line[right] = "."
                        right_len += 1
                        _idx += 1
                        right -= 1
                else:
                    right += right_len
                right_len = 0
            
            elif line[right] == ".":
                right -= 1
    
        result : int = 0
        for x, num in enumerate(line):
            if num != ".":
                result += x * int(num)
        
        return result