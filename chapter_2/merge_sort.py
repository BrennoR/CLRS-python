# merge sort


# Time - O(N log N), Space - O(N)
def merge_sort(A: [int]) -> [int]:
    if A is None:
        return A

    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

    return A


if __name__ == '__main__':
    arr_1 = [1, 5, 7, 3, 8, 5, 9, 32, 4, 124, 8, 45]
    arr_2 = [1, 2, 3, 4, 5, 6]
    arr_3 = [1]
    arr_4 = []
    arr_5 = None
    arr_6 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(arr_1))
    print(merge_sort(arr_2))
    print(merge_sort(arr_3))
    print(merge_sort(arr_4))
    print(merge_sort(arr_5))
    print(merge_sort(arr_6))
