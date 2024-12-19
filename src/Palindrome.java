// https://leetcode.com/problems/palindrome-number/description/
public class Palindrome {
    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length();

        while(left < right)
        {
            if(s.charAt(left) != s.charAt(right))
            {
                return false;
            }
            left++;
            right++;
        }
        return true;
    }
}
