with open("input.txt") as f:
    leftcol, rightcol = zip(*[map(int, line.split()) for line in f])

leftcol = sorted(leftcol)
rightcol = sorted(rightcol)
result = sum(abs(l - r) for l, r in zip(leftcol, rightcol))
print(result)