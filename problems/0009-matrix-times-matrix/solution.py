def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b): return -1
    c = []
    for i in range(len(a)):
        p = []
        for j in range(len(b[0])):
            p.append(sum(a[i][k] * b[k][j] for k in range(len(b))))
        c.append(p)
    return c