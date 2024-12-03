data = open("input.txt").read()


def p1():
	global data
	result = 0

	while len(data) > 3:
		if data[0:4] == "mul(":
			idx = data.index(")")
			temp_data = data[4:idx].split(",")
			if len(temp_data) == 2:
				if temp_data[0].isdigit() and temp_data[1].isdigit():
					result += int(temp_data[0]) * int(temp_data[1])
		data = data[1:]
	print(result)

p1()
