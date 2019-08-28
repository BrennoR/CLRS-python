def counting_sort(arr):
    k = len(arr)
    c = [0] * (k + 1)

    for num in arr:
        c[num[0]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    b = [None] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        b[c[arr[j][0]] - 1] = arr[j][1]
        c[arr[j][0]] -= 1

    return b


# O(d(n + k))
def radix_sort(arr):
    b = arr.copy()

    max_d = max(b)

    while max_d > 0:
        a = []

        for i, num in enumerate(b):
            d = num % 10
            b[i] = b[i] // 10
            a.append(d)

        arr = counting_sort(list(zip(a, arr)))
        b = counting_sort(list(zip(a, b)))

        max_d = max(b)

    return arr


if __name__ == '__main__':
    arr_1 = [123, 432, 643, 752, 895, 458, 679, 304, 100, 344, 267, 123, 825]
    print(radix_sort(arr_1))
