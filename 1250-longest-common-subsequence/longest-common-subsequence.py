class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        ans = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text1)+1):
            ans[0][i] = 0
        
        for j in range(len(text2)+1):
            ans[j][0] = 0

        
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    ans[i][j] = ans[i-1][j-1] + 1
                else:
                    ans[i][j] = max(ans[i-1][j-1], max(ans[i-1][j], ans[i][j-1]))


        return ans[-1][-1]

        