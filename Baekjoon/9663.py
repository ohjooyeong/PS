# N Queen 9663 백준
import sys

N = int(sys.stdin.readline())

col = [0] * 15

def promising(i):
    for j in range(0, i):
        if col[j] == col[i] or abs(col[j]-col[i]) == i - j:
            return False
    return True
def nqueen(col, row):
    global count
    if row == N:
        count += 1
    else:
        for k in range(0, N):
            col[row] = k
            if promising(row):
                nqueen(col, row + 1)
count = 0

nqueen(col, 0)
print(count)
