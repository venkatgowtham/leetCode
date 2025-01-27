// https://leetcode.com/problems/reverse-linked-list/
public class reverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode next = null;
        ListNode current = head;
        if(head != null)
        {
            next = head.next;
        }
        while (current != null) {
            current.next = prev;
            prev = current;
            current = next;
            if (next != null) {
                next = next.next;
            }
        }
        return prev;
    }
}
