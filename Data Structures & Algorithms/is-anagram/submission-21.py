from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)

        for letter in t:
            if letter in s_count:
                s_count[letter] -= 1
                if s_count[letter] < 0:
                    return False
            else:
                s_count[letter] = s_count.get(letter, 0) - 1
        

        return not any(s_count.values())
