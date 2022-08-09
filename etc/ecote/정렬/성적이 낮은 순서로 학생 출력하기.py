n = int(input())

array = []

for i in range(n):
    temp = list(input().split())
    temp[1] = int(temp[1])
    array.append(temp)


# def setting(data):
#     return data[1]


# array = sorted(array, key=setting)


array = sorted(array, key=lambda student: student[1])

for data in array:
    print(data[0], end=" ")
