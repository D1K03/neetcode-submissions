class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx_pairs = {}

        for indx, num in enumerate(nums):
            new_target = target - num

            if new_target in indx_pairs and indx_pairs[new_target] != indx:
                return [indx_pairs[new_target], indx]
            
            indx_pairs[num] = indx
