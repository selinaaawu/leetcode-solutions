class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        ## HEAP | time: O(n log n), space: O(n)
        # repeatedly remove two heaviest stones -> MaxHeap for easy access
        # convert stones to negative value & heapify 
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        # while more than 1 stones remaining
        while len(maxHeap) > 1:
            # pop two heaviest stones
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)

            # push negative difference to heap
            if stone2 > stone1:
                heapq.heappush(maxHeap, stone1 - stone2)

        # return remaining weight or 0
        return -heapq.heappop(maxHeap) if maxHeap else 0
        