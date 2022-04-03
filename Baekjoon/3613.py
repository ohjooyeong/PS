# Java vs C++ 3613

string = input().rstrip()

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def check(string):
    if not string:
        return 2
    if string[0] == "_" or string[0].isupper():
        return 2
    if string[-1] == "_" or "__" in string:
        return 2
    for s in string:
        if s.isupper():
            return 1
    return 0


def trans(string, check):
    ans = ""

    if check:
        for s in string:
            if s == "_":
                return "Error!"
            if s.isupper():
                ans += "_"
                ans += s.lower()
            else:
                ans += s
    else:
        c = 0
        for s in string:
            if s in upper:
                return "Error!"
            if s == "_":
                c = 1
            else:
                if c == 1:
                    ans += s.upper()
                    c = 0
                else:
                    ans += s
    return ans


checked = check(string)
if checked == 2:
    print("Error!")
else:
    print(trans(string, checked))
