class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(s)-1

        for i in range(len(s)//2):
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1
        return True