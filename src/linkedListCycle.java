// https://leetcode.com/problems/linked-list-cycle/submissions/1490626680/
public class linkedListCycle {
    public static boolean detectCycle(LinkedListNode head) {

        // Replace this placeholder return statement with your code
        LinkedListNode slow = head;
        LinkedListNode fast = head;

        while(fast!= null && fast.next!= null)
        {
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast)
            {
                return true;
            }
        }


        return false;
    }
}
