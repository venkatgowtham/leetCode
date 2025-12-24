class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = {}
        result = []
        for i, no in enumerate(nums):
            if target - no in ans:
                result.append(ans[target-no])
                result.append(i)
            else:
                ans[no] = i
        

        return result

        