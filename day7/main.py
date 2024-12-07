from utils.solutionBase import SolutionBase
import re
import time


class solution(SolutionBase):
    data = [line.strip().split(":") for line in open("day7/input.txt").readlines()]
    data_dict = {int(line[0]): list(map(int, line[1].split())) for line in data}


    def get_binary_numbers(self, n):
        return [bin(i)[2:].zfill(n) for i in range(2**n)]


    def get_ternary_numbers(self, n):
        base3 = lambda num: "0" if num == 0 else ''.join(str((num // 3**i) % 3) for i in range(n-1, -1, -1))
        return [base3(i).zfill(n) for i in range(3**n)]
    
    def eval_left_to_right(self, expression: str, max_val=None) -> float:
        tokens = re.findall(r'\d+\.?\d*|[+\-*/]|\|\|', expression)
        
        
        result = tokens[0]
        
        i = 1

        while i < len(tokens):
            operator = tokens[i]
            next_number = tokens[i + 1]

            if operator == '+':
                result = str(int(result) + int(next_number))
            elif operator == '-':
                result = str(int(result) - int(next_number))
            elif operator == '*':
                result = str(int(result) * int(next_number))
            elif operator == '/':
                result = str(int(result) / int(next_number))
            elif operator == '||':                
                result = str(result + next_number)

            if max_val and int(result) > max_val:
                return -1
            
            i += 2
        return int(result)
    

    def p1(self):
        counter = 0
        operations = ["+", "*"]
        for key in self.data_dict:
            possible_operations = self.get_binary_numbers(len(self.data_dict[key]) - 1)
            for operation in possible_operations:
                expression = ""
                idx = 0
                for n in self.data_dict[key][:-1]:
                    expression += str(n) + operations[int(operation[idx])]
                    idx += 1
                expression += str(self.data_dict[key][-1])
                if self.eval_left_to_right(expression) == key:
                    counter += key
                    break
                    
        print(counter)
    
    def p2(self):
        counter = 0
        operations = ["+", "*", "||"]

        num_conted = 0

        for key in self.data_dict:
            num_conted += 1
            print(f"Calculing {num_conted} out of {len(self.data_dict)}")
            possible_operations = self.get_ternary_numbers(len(self.data_dict[key]) - 1)
            for operation in possible_operations:
                expression = ""
                idx = 0
                for n in self.data_dict[key][:-1]:
                    expression += str(n) + operations[int(operation[idx])]
                    idx += 1
                expression += str(self.data_dict[key][-1])
                if self.eval_left_to_right(expression, key) == key:
                    counter += key
                    break
        print(counter)
    
