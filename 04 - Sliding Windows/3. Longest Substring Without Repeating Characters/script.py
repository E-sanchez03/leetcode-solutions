class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        first_letter = s[0]
        sub = s[0]
        output = 1
        for i in s[1:]:
            if i in sub:
                sub = sub[sub.index(i)+1:]
            sub += i
            output = max(output, len(sub))

        return output