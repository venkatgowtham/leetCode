class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0] * 26 
        ans = True

        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1 

        for c in t:
            index = ord(c) - ord('a')
            if count[index] > 0:
                count[index] -= 1
            else:
                ans = False
                return False
        
        val = sum(count)

        if val > 0:
            return False
        else:
            return True
        



        