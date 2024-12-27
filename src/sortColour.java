// https://leetcode.com/problems/sort-colors/description/
public class sortColour {
    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length-1;
        int current = left;

        while (current <= right)
        {
            if(nums[current] == 0)
            {
                int temp = nums[current];
                nums[current] = nums[left];
                nums[left] = temp;
                left++;
                current++;

            }
            else if(nums[current] == 2)
            {
                int temp = nums[current];
                nums[current] = nums[right];
                nums[right] = temp;
                right--;

            }
            else {
                current++;
            }

        }
    }
}
