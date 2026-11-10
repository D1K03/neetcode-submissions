class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = defaultdict(list)

        for word in strs:
            alph = [0] * 26
            for letter in word:
                alph[ord(letter) - ord('a')] += 1
            
            grouped_words[tuple(alph)].append(word)
        
        return list(grouped_words.values())