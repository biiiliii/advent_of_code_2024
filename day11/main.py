from utils.solutionBase import SolutionBase
import copy
from functools import cache

class solution(SolutionBase):
    data = [int(num) for num in open("day11/input.txt").read().split()]

    def p1(self):
        numbers = copy.deepcopy(self.data)

        for _ in range(25):
            new_numbers = list()
            for number in numbers:
                if number == 0:
                    new_numbers.append(1)
                elif len(str(number))%2 == 0:
                    length = len(str(number))
                    new_numbers.append(number // 10**(length//2))
                    new_numbers.append(number % 10**(length//2))
                else:
                    new_numbers.append(number * 2024)
            numbers = new_numbers   
        
        
        return len(new_numbers)
    
    @cache
    def count_stones(self, stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return self.count_stones(1, steps-1)
        l = len(str(stone))
        p = 10**(l//2)
        if l%2 == 0:
            return self.count_stones(stone // p, steps-1) + self.count_stones(stone % p, steps-1)
        return self.count_stones(stone * 2024, steps-1)

    def p2(self):
        return(sum(self.count_stones(number, 75) for number in self.data))
    

