# O(n + k)
def counting_sort(arr):

    k = max(arr)
    c = [0] * (k + 1)

    for num in arr:
        c[num] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    b = [None] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        b[c[arr[j]] - 1] = arr[j]
        c[arr[j]] -= 1

    return b


if __name__ == '__main__':
    A = [4, 3, 16, 86, 34, 63, 8, 9, 23, 200, 100, 23, 48]
    print(counting_sort(A))
