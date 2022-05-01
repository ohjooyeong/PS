# IPv6 3107 백준


ip = input()

arr = ip.split(":")

if arr.count(""):
    if len(arr) > 8:
        del arr[arr.index("")]
    while len(arr) < 8:
        arr.insert(arr.index(""), "0000")

for i in range(8):
    arr[i] = (4 - len(arr[i])) * "0" + arr[i]

print(":".join(arr))
