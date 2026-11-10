class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = defaultdict(list)

        for word in strs:
            grouped_words[''.join(sorted(word))].append(word)

        return list(grouped_words.values())
