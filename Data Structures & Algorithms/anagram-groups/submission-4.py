from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for s in strs:
            grouped[''.join(sorted(s))].append(s)
        
        return list(grouped.values())