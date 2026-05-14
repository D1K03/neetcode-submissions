class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)

        for l in t:
            s_count[l] -= 1

        
        for count in s_count.values():
            if count != 0:
                return False
        
        return True

        