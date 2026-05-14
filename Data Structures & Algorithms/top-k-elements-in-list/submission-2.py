class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        out = []

        pairs = list(tuple(num_count.items()))
        pairs.sort(key=lambda p:p[1], reverse=True)

        for i in range(k):
            out.append(pairs[i][0])

        return out