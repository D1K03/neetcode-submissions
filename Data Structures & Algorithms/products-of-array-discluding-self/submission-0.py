class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 0
        sumList = []
        while c < len(nums):
            summation = 1
            for i in range(len(nums)):
                if i == c:
                    continue
                else:
                    summation *= nums[i]
            sumList.append(summation)
            c += 1
        return sumList
        


        