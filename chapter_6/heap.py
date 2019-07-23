import unittest


class Heap:

    def __init__(self, A=None):
        self.data = [0]
        self.size = 0
        if A:
            self.data.extend(A)
            self.size = len(A)
            self.build_max_heap()

    def insert(self, element):
        self.data.append(element)
        self.size += 1
        self.max_heapify_up(self.size)

    def extract_max(self):
        if self.size < 1:
            raise Exception("heap underflow")

        val = self.data[1]
        self.data[1] = self.data[self.size]
        self.data.pop()
        self.size -= 1
        self.max_heapify_down(1)
        return val

    def increase_key(self):
        pass

    def maximum(self):
        if self.size > 0:
            return self.data[1]

    def max_heapify_up(self, i):
        p = i // 2
        while p > 0 and self.data[p] < self.data[i]:
            tmp = self.data[p]
            self.data[p] = self.data[i]
            self.data[i] = tmp
            i = p
            p = i // 2

    def max_heapify_down(self, i):
        left = i * 2
        right = i * 2 + 1

        if left <= self.size and self.data[left] > self.data[i]:
            largest = left
        else:
            largest = i
        if right <= self.size and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            tmp = self.data[largest]
            self.data[largest] = self.data[i]
            self.data[i] = tmp
            self.max_heapify_down(largest)

    def build_max_heap(self):
        self.size = len(self.data) - 1
        for i in range(self.size // 2, 0, -1):
            self.max_heapify_down(i)

        return self.data

    def heapsort(self):
        for i in range(self.size, 1, -1):
            tmp = self.data[1]
            self.data[1] = self.data[i]
            self.data[i] = tmp
            self.size -= 1
            self.max_heapify_down(1)

        return self.data


class HeapTests(unittest.TestCase):

    def test_max_heap(self):
        heap = Heap(A=[5, 4, 2, 7, 2, 71, 5, 2, 1, 1, 1, 6, 7, 8, 9, 200])
        self.verify_max_heap(heap)

    def test_heap_sort(self):
        heap = Heap(A=[5, 4, 2, 7, 2, 71, 5, 2, 1, 1, 1, 6, 7, 8, 9, 200])
        size = heap.size
        heap.heapsort()
        for i in range(size - 1):
            self.assertTrue(heap.data[i] <= heap.data[i + 1])

    def test_build_max(self):
        heap = Heap(A=[5, 4, 2, 7, 2, 71, 5, 2, 1, 1, 1, 6, 7, 8, 9, 200])
        heap.heapsort()
        heap.build_max_heap()
        self.verify_max_heap(heap)

    def verify_max_heap(self, heap):
        for i in range(heap.size // 2, 0, -1):
            left = i * 2
            right = i * 2 + 1
            if left <= heap.size:
                self.assertTrue(heap.data[i] >= heap.data[left])
            if right <= heap.size:
                self.assertTrue(heap.data[i] >= heap.data[right])


if __name__ == '__main__':
    unittest.main()
