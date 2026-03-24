class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0 
        seen_map = {}
        index = 0
        ans = 0
        for ch in s:
            if ch in seen_map and seen_map[ch] >= start:
                ans = max(ans, index - start)
                start = seen_map[ch] + 1
            seen_map[ch] = index
            index += 1
        ans = max(ans, index - start)

        return ans
        



        