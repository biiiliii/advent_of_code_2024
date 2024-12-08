from utils.solutionBase import SolutionBase

class solution(SolutionBase):
	
	with open("day2/input.txt") as f:
		data = [list(map(int, line.split())) for line in f]

	def p1(self):
		safe_count = 0
		for lst in self.data:
			if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
				if all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:])):
					safe_count += 1 
		return safe_count

	def p2(self):
		safe_count = 0
		for lst in self.data:
			valid = False
			if sorted(lst) == lst or sorted(lst, reverse=True) == lst:
				if all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:])):
					safe_count += 1
					valid = True
			if not valid:
				for i in range(len(lst)):
					new_lst = lst[:i] + lst[i+1:]
					if (sorted(new_lst) == new_lst or sorted(new_lst, reverse=True) == new_lst) and \
						all(1 <= abs(a - b) <= 3 for a, b in zip(new_lst, new_lst[1:])):
						safe_count += 1
						break
		return safe_count

	
