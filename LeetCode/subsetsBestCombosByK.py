from heapq import heappush, heappop


def bestCombo(popularity, k):
    heap = []
    heappush(heap, 0)

    for i in popularity:
        prev_h = heap.copy()
        for nums in prev_h:
            push_element = -float('inf')
            if len(heap) == k:
                push_element = heappop(heap)
            heappush(heap, max(push_element, nums + i))
    return sorted(heap, reverse=True)


popularity = [1, 2, 3, 1000]
k = 4


print(bestCombo(popularity, k))
