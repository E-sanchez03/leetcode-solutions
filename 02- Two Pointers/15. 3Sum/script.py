from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
    
        for x in range(len(nums)):
            if nums[x] > 0:
                break
            if x > 0 and nums[x] == nums[x-1]:
                continue
            left = x+1
            right = len(nums) -1
            while left < right:
                trip = [nums[x], nums[left], nums[right]]
                total = sum(trip)
                if total >0:
                    right -= 1
                elif total <0:
                    left +=1
                
                else:
                    triplets.append(trip)
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left += 1
           
        return triplets