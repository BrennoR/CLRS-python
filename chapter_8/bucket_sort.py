from math import floor
from chapter_2.insertion_sort import insertion_sort


# O(n)
def bucket_sort(arr):
    n = len(arr)
    b = [[] for _ in range(n)]

    for i in range(n):
        b[floor(n * arr[i])].append(arr[i])

    for i in range(n):
        b[i] = insertion_sort(b[i])

    c = []
    for nums in b:
        c.extend(nums)

    return c


if __name__ == '__main__':
    arr_1 = [.89, .24, .12, .34, .32, .95, .60, .43, .65, .55]
    print(bucket_sort(arr_1))

