class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat_arr = [0] * (2*n)
        
        for idx, num in enumerate(nums):
            concat_arr[idx] = num
            concat_arr[idx+n] = num

        return concat_arr