class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = [0] * 26 
        ans = True

        for c in range(len(s)):
            index = ord(s[c]) - ord('a')
            count[index] += 1 
            index = ord(t[c]) - ord('a')
            count[index] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True
        



        