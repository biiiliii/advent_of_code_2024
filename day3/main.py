from utils.solutionBase import SolutionBase

class solution(SolutionBase):
	data = open("day3/input.txt").read()

	def p1(self):
		used_data = self.data
		result = 0
		while len(used_data) > 3:
			if used_data[0:4] == "mul(":
				idx = used_data.index(")")
				temp_data = used_data[4:idx].split(",")
				if len(temp_data) == 2:
					if temp_data[0].isdigit() and temp_data[1].isdigit():
						result += int(temp_data[0]) * int(temp_data[1])
			used_data = used_data[1:]
		print(result)

	def p2(self):
		used_data = self.data
		result = 0
		enabled = True
		while len(used_data) > 4:
			if used_data[0:4] == "do()":
				enabled = True
			if used_data[0:7] == "don't()":
				enabled = False
			if enabled:
				if used_data[0:4] == "mul(":
					idx = used_data.index(")")
					temp_data = used_data[4:idx].split(",")
					if len(temp_data) == 2:
						if temp_data[0].isdigit() and temp_data[1].isdigit():
							result += int(temp_data[0]) * int(temp_data[1])
			used_data = used_data[1:]
		print(result)

