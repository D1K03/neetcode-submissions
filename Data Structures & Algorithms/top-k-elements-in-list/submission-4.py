class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea 1: counter, store key value in a tuple, store each tuple in a list then sort by value
        num_count = Counter(nums)
        num_pairs = []

        for num, count in num_count.items():
            num_pairs.append((num, count))

        num_pairs.sort(key=lambda pair: pair[1], reverse=True)
        
        return [num_pairs[i][0] for i in range(k)]   