def solution(S):
    files = S.split("\n")
    file_arr = []
    for file in files:
        file_arr.append(file.split())
    for i in range(len(file_arr)):
        if file_arr[i][0] == "admin":
            if file_arr[i][1][-1] == "x":
                if int(file_arr[i][5]) < (14 * 2 ** 20):
                    ans = f"{file_arr[i][2]} {file_arr[i][3]} {file_arr[i][4]}"
                    return ans
    return "NO FILES"


test2 = """admin  -wx 29 Sep 1983        833 source.h
admin  r-x 23 Jun 2003     854016 blockbuster.mpeg
admin  --x 02 Jul 1997        821 delete-this.py
admin  -w- 15 Feb 1971      23552 library.dll
admin  --x 15 May 1979  645922816 logs.zip
jane   --x 04 Dec 2010      93184 old-photos.rar
jane   -w- 08 Feb 1982  681574400 important.java
admin  rwx 26 Dec 1952   14680064 to-do-list.txt"""

print(solution(test2))
