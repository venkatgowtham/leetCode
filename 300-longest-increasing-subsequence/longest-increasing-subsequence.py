class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = [1 for _ in nums]
        result = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:

                    if 1 + ans[j] > ans[i]:
                        ans[i] = 1 + ans[j]
                        if ans[i] > result:
                            result = ans[i]
        
        return result 






        