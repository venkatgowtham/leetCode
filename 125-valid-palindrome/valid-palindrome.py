class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s)-1
        s= lower(s)
        while left <= right:
            while left < right and not(s[left] >= 'a' and s[left]<='z') and not(s[left] >= '0' and s[left]<='9'):
                left+=1
            while left < right and not(s[right] >= 'a' and s[right]<='z') and not(s[right] >= '0' and s[right]<='9'):
                right -=1
            if s[left] != s[right]:
                return False
            left +=1 
            right -= 1
        
        return True


        