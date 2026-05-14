class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0

        for r in range(len(nums)):
            if l == r:
                continue
            
            if nums[l] == nums[r]:
                return True
            
            l += 1
        
        return False