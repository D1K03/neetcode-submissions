class Solution:
    def isPalindrome(self, s: str) -> bool:
        merged = []

        for letter in s:
            if letter.isalnum():
                merged.append(letter.lower())
        
        alphaString = "".join(merged)

        return  alphaString == alphaString[::-1]


        