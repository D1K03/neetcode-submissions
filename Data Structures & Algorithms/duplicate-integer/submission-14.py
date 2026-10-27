class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0

        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                return True
            l = r
        
        return False
        