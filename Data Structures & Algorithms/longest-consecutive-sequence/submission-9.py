class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return len(nums)
        
        nums_s = set(nums)

        curr = 1
        longest = 1

        for num in nums_s:
            temp = num
            while temp+1 in nums_s:
                curr += 1
                temp += 1
            longest = max(longest,curr)
            curr = 1
        
        return longest