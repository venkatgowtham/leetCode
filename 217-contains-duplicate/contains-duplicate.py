class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value_map = {}

        for no in nums:
            if no in value_map:
                return True
            else:
                value_map[no] =1 
        return False
        