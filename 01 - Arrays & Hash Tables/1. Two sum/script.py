from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,x in enumerate(nums):
            i_res = hash_map.get(target-x,-1)
            if i_res != -1:
                return i_res,i
            else:
                hash_map[x] = i