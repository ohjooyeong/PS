n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))
nCnt = 0
mCnt = 0
ans = []
while nCnt < n and mCnt < m:
    if nList[nCnt] <= mList[mCnt]:
        ans.append(nList[nCnt])
        nCnt += 1
    else:
        ans.append(mList[mCnt])
        mCnt += 1

if nCnt == n:
    for i in range(mCnt, m):
        ans.append(mList[i])
else:
    for j in range(nCnt, n):
        ans.append(nList[j])

print(ans)
