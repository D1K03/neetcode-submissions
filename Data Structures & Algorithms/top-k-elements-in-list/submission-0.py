class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        pairs = list(num_count.items())
        pairs.sort(key=lambda pair:pair[1], reverse=True)

        out = []

        for i in range(k):
            out.append(pairs[i][0])

        return out