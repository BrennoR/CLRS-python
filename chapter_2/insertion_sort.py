# insertion sort


# Time - O(N^2), Space - O(1), efficient for a small number of elements, in-place algorithm
def insertion_sort(arr: [int]) -> [int]:
    if arr is None:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr_1 = [1, 5, 7, 3, 8, 5, 9, 32, 4, 124, 8, 45]
    arr_2 = [1, 2, 3, 4, 5, 6]
    arr_3 = [1]
    arr_4 = []
    arr_5 = None
    arr_6 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insertion_sort(arr_1))
    print(insertion_sort(arr_2))
    print(insertion_sort(arr_3))
    print(insertion_sort(arr_4))
    print(insertion_sort(arr_5))
    print(insertion_sort(arr_6))
