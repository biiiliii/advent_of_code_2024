from utils.solutionBase import SolutionBase
import re

class solution(SolutionBase):
    data = open("day17/input.txt").read()


    def p1(self):
        rA, rB, rC, *program = map(int, re.findall(r"\d+", self.data))

        instruction_pointer = 0
        value = ""
        while (instruction_pointer < len(program)):
            opcode = program[instruction_pointer]
            operand = program[instruction_pointer + 1]
            if operand == 4:
                combo_operand = rA
            elif operand == 5:
                combo_operand = rB
            elif operand == 6:
                combo_operand = rC
            else:
                combo_operand = operand
    
            if opcode == 0: #adv
                rA = rA >> combo_operand
            elif opcode == 1: #bxl
                rB = rB ^ operand
            elif opcode == 2: #bst
                rB = combo_operand % 8
            elif opcode == 3: #jnz
                if rA != 0:
                    instruction_pointer = operand
                    continue
            elif opcode == 4: #bxc
                rB = rB ^ rC
            elif opcode == 5: #out
                value += str(combo_operand % 8)
            elif opcode == 6: #bdv
                rB = rA >> combo_operand
            elif opcode == 7: #cdv
                rC = rA >> combo_operand
            
            instruction_pointer += 2
        
        print(f"Register A: {rA}, Register B: {rB}, Register C: {rC}")
        return ",".join(value) 