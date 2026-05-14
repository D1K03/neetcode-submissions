class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""

        for letter in s:
            if letter.isalnum():
                clean_s += letter.lower()

        words = clean_s.split(" ")
        palin = ''.join(words)

        return palin == palin[::-1]

        