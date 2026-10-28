class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {num1: idx1 for idx1, num1 in enumerate(nums)}
        
        for idx2, num2 in enumerate(nums):
            new_target = target - num2
            if new_target in num_idx and idx2 != num_idx[new_target]:
                return [idx2, num_idx[new_target]]