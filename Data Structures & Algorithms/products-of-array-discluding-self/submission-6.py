class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1
        out = []

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total *= num
        
        for num in nums:
            if num == 0:
                if zero_count > 1:
                    out.append(0)
                else:
                    out.append(total)
            else:
                if zero_count > 0:
                    out.append(0)
                else:
                    except_self = total // num
                    out.append(except_self)
        
        return out
