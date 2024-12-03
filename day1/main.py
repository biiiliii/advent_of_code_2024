with open("input.txt") as f:
    leftcol, rightcol = zip(*[map(int, line.split()) for line in f])

def p1():
    global leftcol, rightcol
    leftcol = sorted(leftcol)
    rightcol = sorted(rightcol)
    result = sum(abs(l - r) for l, r in zip(leftcol, rightcol))
    print(result)

def p2():
    global leftcol, rightcol
    result = sum(n * rightcol.count(n) for n in leftcol)
    print(result)

p1()
p2()