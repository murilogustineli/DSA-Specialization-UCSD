import sys


def merge(array, left, right):
    inversions = 0
    output = []

    while len(left) and len(right) > 0:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
            inversions += len(left)

    output += left or right
    return output, inversions


def mergeSort(array):
    if len(array) == 1:
        return array, 0

    mid = len(array)//2

    left, x = mergeSort(array[:mid])
    right, y = mergeSort(array[mid:])
    merged, z = merge(array, left, right)

    return merged, x+y+z


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    sorted_array, inversion = mergeSort(elements)
    print(inversion)
