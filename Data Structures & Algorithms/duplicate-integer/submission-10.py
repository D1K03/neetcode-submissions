class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)

        for v in num_count.values():
            if v > 1:
                return True
        
        return False
        