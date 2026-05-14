class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for indx, num in enumerate(numbers):
            new_target = target - num

            l, r = 0, len(numbers)-1

            while l <= r:
                mid = (l + r) // 2

                if new_target > numbers[mid]:
                    l = mid + 1
                
                elif new_target < numbers[mid]:
                    r = mid - 1
                
                else:
                    return [indx+1, mid+1]
        