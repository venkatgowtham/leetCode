from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value_count = {}

        ans = 0

        for n in nums:
            if n in value_count:
                continue
            
            left = value_count.get(n-1,0)
            right = value_count.get(n+1, 0)
            val = left + right + 1
            value_count[n] = val
            value_count[n-left]= val
            value_count[n+right]= val
            if val > ans:
                ans = val
        return ans
