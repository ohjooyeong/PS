def DFS(x):
    if x == 0:
        return
    DFS(x - 1)
    print(x, end=" ")


DFS(10)
