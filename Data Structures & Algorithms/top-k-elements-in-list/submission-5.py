import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea 1: counter, store key value in a tuple, store each tuple in a list then sort by value
        # idea 2: max heap
        num_count = Counter(nums)
        num_pairs = []

        for num, count in num_count.items():
            num_pairs.append((num, count))
        
        freq_pairs = heapq.nlargest(k, num_pairs, key=lambda pair:pair[1])
        
        return [pair[0] for pair in freq_pairs]
