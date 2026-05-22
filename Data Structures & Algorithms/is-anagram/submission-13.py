class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)

        for letter in t:
            if letter not in s_count:
                return False
            
            s_count[letter] -= 1

            if s_count[letter] < 0:
                return False


        return True
        