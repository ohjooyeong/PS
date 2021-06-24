n = int(input())
arr = list(map(int, input().split()))
check = [0] * n
ans = "NO"


def dfs(v):
    global ans
    if n == (v + 1):
        c1 = []
        c2 = []
        for i in range(n):
            if check[i] == 1:
                c1.append(arr[i])
            else:
                c2.append(arr[i])
        if sum(c1) == sum(c2):
            ans = "YES"
    else:
        check[v] = 1
        dfs(v + 1)
        check[v] = 2
        dfs(v + 1)


dfs(0)
print(ans)

# import sys


# def dfs(L, sum):
#     if sum > total // 2:
#         return
#     if L == n:
#         if sum == (total - sum):
#             print("YES")
#             sys.exit(0)
#         else:
#             dfs(L + 1, sum + arr[L])
#             dfs(L + 1, sum)


# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#     total = sum(a)
#     dfs(0, 0)
