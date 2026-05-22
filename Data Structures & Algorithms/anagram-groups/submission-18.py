class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            alpha = [0] * 26

            for letter in word:
                alpha[ord(letter) - ord('a')] += 1
        
            groups[tuple(alpha)].append(word)
        
        return list(groups.values())