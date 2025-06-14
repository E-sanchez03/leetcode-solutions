from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [nums[0]] * n
        suf_prod = [1] * n
        
        for i in range(n-2,-1,-1):
            suf_prod[i] = suf_prod[i+1]*nums[i+1]
        
        for i in range(1, n):
            pre_prod[i] = nums[i] * pre_prod[i-1]
            suf_prod[i] *= nums[i]
        output = [1]*n
        output[0] = suf_prod[1]
        for i in range(1,n-1):
            output[i] = suf_prod[i+1] * pre_prod[i-1]
        output[-1] = pre_prod[-2]
        return output