def solution(S, C):
    arr = S.replace("-", "").split(", ")
    assist_arr = S.split(", ")
    C = C.lower()
    C = f"@{C}.com"
    res = []
    nick = []
    ans = ""
    for i in range(len(arr)):
        arr[i] = arr[i].split()

    for i in range(len(arr)):
        email = ""
        n = len(arr[i])
        for j in range(n - 1):
            email += arr[i][j].lower()[0]
        email += arr[i][n - 1].lower()[:8]
        cnt = 1
        for k in nick:
            if k == email:
                cnt += 1
        nick.append(email)
        if cnt != 1:
            email += str(cnt)
        email += C
        res.append(email)
    for i in range(len(assist_arr)):
        ans += f"{assist_arr[i]} <{res[i]}>"
        if i < len(arr) - 1:
            ans += ", "
    return ans


print(
    solution(
        "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker",
        "Example",
    )
)
