class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indx1, num1 in enumerate(nums):
            for indx2, num2 in enumerate(nums):
                if indx1 == indx2:
                    continue
                
                if num1 + num2 == target:
                    return [indx1, indx2]
        