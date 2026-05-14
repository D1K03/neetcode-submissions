import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea 1: counter, store key value in a tuple, store each tuple in a list then sort by value
        # idea 2: max heap
        num_count = Counter(nums)
        max_heap = []
        
        for num, count in num_count.items():
            heapq.heappush_max(max_heap, (count, num))
        
        return [heapq.heappop_max(max_heap)[1] for i in range(k)]
    
