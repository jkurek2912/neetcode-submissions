class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        heap = []
        for key, value in map.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
