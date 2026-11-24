class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        x = y = 0
        final = 0
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            y = abs(heapq.heappop(heap))
            x = abs(heapq.heappop(heap))

            if x != y:
                res = y - x
                heapq.heappush(heap, -res)
        if len(heap) == 1:
            final = heapq.heappop(heap)
        return abs(final)