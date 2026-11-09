class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        '''
        - ALL STRINGS
        - Longest can be at most length of shortest string
        - Shortest can be "" string whern first letters don't match
        - String in array's CAN be empty, e.g. ["", "jam", "jacket"]
        - Array CAN'T be empty
        - No need to check for capitalisations, all lowercase
        '''

        if len(strs) == 1:
            return strs[0]

        
        shortest_length = len(min(strs, key=len))
        prefix = ""

        for i in range(shortest_length):
            prev = ""
            for j in range(len(strs)):
                if not prev:
                    prev = strs[j][i]
                    continue
                    
                curr = strs[j][i]
                if curr  != prev:
                    return prefix
            prefix += curr

        return prefix

