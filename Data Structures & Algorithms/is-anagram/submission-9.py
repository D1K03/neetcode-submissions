class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # implementing Counter manually
        t_count = {}

        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        for letter in s:
            t_count[letter] = t_count.get(letter, -1) - 1


        for v in t_count.values():
            if v != 0:
                return False
        
        return True