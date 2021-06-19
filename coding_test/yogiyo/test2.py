def solution(U, L, C):
    if sum(C) != (U + L):
        return "IMPOSSIBLE"
    u_arr = [0] * len(C)
    l_arr = [0] * len(C)
    t_c = sum(C)
    u_c = U
    l_c = L
    idx = 0
    ans = ""
    flag1 = 1
    flag2 = 1
    while idx < len(C):
        if C[idx] == 2:
            u_arr[idx] = 1
            l_arr[idx] = 1
            u_c -= 1
            l_c -= 1
        elif C[idx] == 1:
            if u_c > 0 and flag1:
                u_arr[idx] = 1
                u_c -= 1
                flag1 = 0
                flag2 = 1
            elif l_c > 0 and flag2:
                l_arr[idx] = 1
                l_c -= 1
                flag1 = 1
                flag2 = 0
            if flag2 == 0 and flag1 == 0:
                flag1 = 1
                flag2 = 1
        idx += 1
    u_str = "".join(map(str, u_arr))
    l_str = "".join(map(str, l_arr))
    ans = f"{u_str} {l_str}"
    return ans


print(solution(2, 2, [2, 0, 2, 0]))
