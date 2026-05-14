class Solution:
    def isPalindrome(self, s: str) -> bool:
        wholeString = ''.join(s.split(" "))
        for char in wholeString:
            if not char.isalnum():
                wholeString = wholeString.replace(char, '')
        
        return wholeString.lower() == wholeString[::-1].lower()
        