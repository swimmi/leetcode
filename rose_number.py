for i in range(1000, 10000, 4):
    x, y = str(i), 0
    for j in range(4):
        y += int(x[j]) ** 4
    if i == y:
        print(i)