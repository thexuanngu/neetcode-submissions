class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for letter in s:
            if letter.isalnum():
                letters.append(letter.lower())
        left = 0
        right = len(letters) - 1
        while left < right:
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        return True
        