from utils.solutionBase import SolutionBase

class solution(SolutionBase):
	def __init__(self, day: int, part: int):
		self.day = day
		self.part = part
		with open("day1/input.txt") as f:
			self.leftcol, self.rightcol = zip(*[map(int, line.split()) for line in f])

	def p1(self):
		self.leftcol = sorted(self.leftcol)
		self.rightcol = sorted(self.rightcol)
		result = sum(abs(l - r) for l, r in zip(self.leftcol, self.rightcol))
		print(result)

	def p2(self):
		result = sum(n * self.rightcol.count(n) for n in self.leftcol)
		print(result)
