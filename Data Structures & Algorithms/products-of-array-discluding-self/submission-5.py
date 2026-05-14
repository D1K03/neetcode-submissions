class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        total = 1
        for num1 in nums:
            if num1 != 0:
                total *= num1
        
        print(total)

        out = []

        for num2 in nums:
            if 0 in counts:
                if num2 == 0 and counts[num2] > 1:  
                    out.append(0)

                elif num2 != 0:
                    out.append(0)

                else:
                    out.append(total)
            else:
                out.append(total//num2)

        return out
        