class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for idx, letter in enumerate(t):
            if letter != s[idx]:
                return False
        
        return True
        