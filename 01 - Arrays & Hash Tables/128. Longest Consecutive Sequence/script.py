from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        counts = 0
        for n in nums:
            if n+1 in nums:
                continue
            count =1
            c = n-1
            while c in nums:
                count+=1
                c-=1
            counts = max(counts,count)
        return counts