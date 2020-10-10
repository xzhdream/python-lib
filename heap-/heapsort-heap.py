from heapq import heappush, heappop


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
        print('l',h)
    x = [heappop(h) for i in range(len(h))]
    print('0',x)

x = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(x)
