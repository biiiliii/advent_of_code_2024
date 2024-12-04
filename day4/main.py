data = [line.strip() for line in open("input.txt").readlines()]

def p1():
    global data

    f, c = len(data), len(data[0])
    comptador = 0

    for i in range(f):
        comptador += data[i].count("XMAS")
        comptador += data[i][::-1].count("XMAS")
    vertical_data = list(map("".join, zip(*data)))
    for i in range(f):
        comptador += vertical_data[i].count("XMAS")
        comptador += vertical_data[i][::-1].count("XMAS")

    for i in range(f - 3):
        for j in range(c - 3):
            diagonal = "".join([data[i + k][j + k] for k in range(4)])
            comptador += diagonal.count("XMAS")
            comptador += diagonal[::-1].count("XMAS")
    for i in range(3, f):
        for j in range(c - 3):
            diagonal = "".join([data[i - k][j + k] for k in range(4)])
            comptador += diagonal.count("XMAS")
            comptador += diagonal[::-1].count("XMAS") 
    print(comptador)

def p2():
    global data

    f, c = len(data), len(data[0])
    comptador = 0

    for i in range(1, f - 1):
        for j in range(1, c - 1):
            if data[i][j] == 'A':
                diagonal_right = "".join([data[i + k][j + k] for k in range(-1, 2)])
                diagonal_left = "".join([data[i - k][j + k] for k in range(-1, 2)])
                if (diagonal_left.count("MAS") + diagonal_left[::-1].count("MAS")) and (diagonal_right.count("MAS") + diagonal_right[::-1].count("MAS")):
                    comptador += 1

    print(comptador)

p1()
p2()
