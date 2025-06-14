from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        counts = []
        def check(n):
            suma = 1
            if n in nums:
                suma += check(n-1)
            return suma
        for n in nums:
            if n+1 in nums:
                continue
            count = check(n-1)
            counts.append(count)
        
        return max(counts)