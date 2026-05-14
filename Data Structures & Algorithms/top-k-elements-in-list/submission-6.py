import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea 1: counter, store key value in a tuple, store each tuple in a list then sort by value
        # idea 2: max heap
        num_count = Counter(nums)
        
        return heapq.nlargest(k, num_count.keys(), key=lambda num:num_count.get(num))
    
