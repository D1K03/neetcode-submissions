class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        out = [0] * len(nums)

        curr = 1
        for num in nums:
            curr *= num
            prefix.append(curr)
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            curr *= nums[i]
            suffix[i] = curr
        

        for idx, num in enumerate(nums):
            pre = 1
            post = 1

            if idx != 0:
                pre = prefix[idx-1]
            
            if idx != len(nums)-1:
                post = suffix[idx+1]
            
            out[idx] = pre * post
        
        return out
                
        '''
        nums = [1, 2, 4, 6]
        prefix = [1, 2, 8, 48]
        suffix = [1, 48, 24, 6]
        out = [48, 24, 12, 8]

        '''

