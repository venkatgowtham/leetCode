// https://leetcode.com/problems/happy-number/
public class happyNumber {
    public boolean isHappy(int n) {
        int s = n;
        int f = sumOfSuaresOfDigits(n);

        while(s!=f && f!=1 && s!=1)
        {
            s = sumOfSuaresOfDigits(s);
            f = sumOfSuaresOfDigits(sumOfSuaresOfDigits(f));
        }

        if(f==1)
        {
            return true;
        }
        else
        {
            return false;
        }

    }

    int sumOfSuaresOfDigits(int x){
        int sum = 0;
        while(x>0)
        {
            int y = x % 10;
            sum = sum + (int)Math.pow(y, 2);
            x=x/10;
        }
        return sum;
    }
}
