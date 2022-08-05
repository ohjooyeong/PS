array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    rigth_side = [x for x in tail if x > pivot]

    return quickSort(left_side) + [pivot] + quickSort(rigth_side)
