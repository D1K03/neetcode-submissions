class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}

        for idx, num in enumerate(nums):
            num_idx[num] = idx

        for idx, num in enumerate(nums):
            newTarget = target - num
            if newTarget in num_idx and idx != num_idx[newTarget]:
                return [idx, num_idx[newTarget]]
        