from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying= prices[0]
        selling = 0
        for i in prices:
            buying = min(buying,i)
            selling = max(selling,i-buying)
        return selling