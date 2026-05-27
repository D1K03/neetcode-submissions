class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        nums = [2,20,4,10,3,4,5]
        out = 4 -> [2,3,4,5]
        
        - Can a set be used? We only ever consider 1 onccurence in a sequence
        - O(n) time, no sorting

        '''
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        num_set = set(nums)
    
        chain = 1
        long_chain = -1


        for num in num_set:
            if num + 1 in num_set:
                temp = num
                while temp + 1 in num_set:
                    temp += 1
                    chain += 1
        
            long_chain = max(long_chain, chain)
            chain = 1

        return long_chain


        '''
        nums = [9,1,4,7,3,-1,0,5,8,0,-1,6]
        num_set = {9,1,4,7,3,-1,0,5,8,6}
        itr = 0
        curr = -1
        chain = 1
        long_chain = -1

        curr = 0
        chain = 2
        curr = 1
        chain = 3

        long_chain = 3

        chain = 1
        curr = 2

        '''
            



        