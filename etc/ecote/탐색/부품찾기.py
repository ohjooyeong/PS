n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


arr1.sort()

for num in arr2:
    if binary_search(arr1, num, 0, n - 1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
