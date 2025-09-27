class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sofar = nums[0]
        max_sofar = nums[0]
        result = nums[0]

        for n in nums[1:]:
            
            if n < 0:
                min_sofar, max_sofar = max_sofar, min_sofar
            
            max_sofar = max(n, max_sofar*n)
            min_sofar = min(n, min_sofar*n)

            result = max(result, max_sofar) 

        return result






        