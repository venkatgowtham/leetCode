public class reverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode next = head.next;
        ListNode current = head;

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
