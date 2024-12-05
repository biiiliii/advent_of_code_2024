class SolutionBase:
	def __init__(self, day: int, part: int):
		self.day = day
		self.part = part

	def p1(self):
		print("No solution for part 1")
	def p2(self):
		print("No solution for part 2")

	def solve(self):
		if self.part == 1:
			self.p1()
		elif self.part == 2:
			self.p2()
		elif self.part == None:
			self.p1()
			self.p2()