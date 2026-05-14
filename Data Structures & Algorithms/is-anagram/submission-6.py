class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)

        for letter in t:
            if letter in t:
                s_count[letter] -= 1

        
        for count in s_count.values():
            if count != 0:
                return False
        
        return True
        
    