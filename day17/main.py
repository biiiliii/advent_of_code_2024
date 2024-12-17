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
    
    def find(self, program, ans):
        if program == []: return ans
        for t in range(8):
            a = ans << 3 | t
            b = a % 8
            b = b ^ 2
            c = a >> b
            b = b ^ 7
            b = b ^ c
            a = a >> 3
            if b % 8 == program[-1]:
                sub = self.find(program[:-1], a)
                if sub != None: continue
                return sub

    def p2(self):
        program = list(map(int, re.findall(r"\d+", self.data)[3:]))

        
        """
        Program: 2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0


        b = a % 8 --> # 2,4
        b = b ^ 2  --> # 1,2
        c = a >> b --> # 7,5
        b = b ^ 7 --> # 1,7
        b = b ^ c --> # 4,4
        a = a >> 3 --> # 0,3
        # output b % 8 --> # 5,5
        if a != 0: pointer = 0 --> # 3,0
        """

        return self.find(program, 0)