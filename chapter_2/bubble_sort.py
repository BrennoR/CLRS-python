# bubble sort


# Time - O(N^2), Space - O(1)
def bubble_sort(A: [int]) -> [int]:
    if A is None:
        return A

    for _ in range(len(A) - 1):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp

    return A


# bubble sort with early stopping
def bubble_sort_short(A: [int]) -> [int]:
    if A is None:
        return A

    sorted = False
    while not sorted:
        sorted = True
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp
                sorted = False

    return A


if __name__ == '__main__':
    arr_1 = [1, 5, 7, 3, 8, 5, 9, 32, 4, 124, 8, 45]
    arr_2 = [1, 2, 3, 4, 5, 6]
    arr_3 = [1]
    arr_4 = []
    arr_5 = None
    arr_6 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(arr_1))
    print(bubble_sort(arr_2))
    print(bubble_sort(arr_3))
    print(bubble_sort(arr_4))
    print(bubble_sort(arr_5))
    print(bubble_sort(arr_6))
    print(bubble_sort_short(arr_1))
    print(bubble_sort_short(arr_2))
    print(bubble_sort_short(arr_3))
    print(bubble_sort_short(arr_4))
    print(bubble_sort_short(arr_5))
    print(bubble_sort_short(arr_6))
