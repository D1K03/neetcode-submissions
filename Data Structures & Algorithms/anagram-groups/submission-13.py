class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for letter in s:
                freq[ord(letter) - ord('a')] += 1
            
            groups[tuple(freq)].append(s)
        
        return list(groups.values())