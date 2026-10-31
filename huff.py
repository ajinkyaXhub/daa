import heapq

chars = ['A', 'B', 'C', 'D', 'E']
freq = [5, 9, 12, 13, 16]

heap = [[freq[i], chars[i]] for i in range(len(chars))]
heapq.heapify(heap)

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    for c in left[1:]:
        print(c, "-> 0", end="  ")

    for c in right[1:]:
        print(c, "-> 1", end="  ")

    heapq.heappush(heap, [left[0] + right[0], left[1:] + right[1:]])

print("\nHuffman Encoding completed")
