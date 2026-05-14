class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0

        for r, num in enumerate(nums):
            if r == l:
                continue
            
            if num == nums[l]:
                return True
            
            l = r
        
        return False