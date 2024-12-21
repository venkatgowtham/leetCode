//https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
public class remove_nth_node_from_end_of_list {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        int i = 0;
        ListNode leftNode = head;
        ListNode rightNode = head;
        while (i<n)
        {
            rightNode = rightNode.next;
        }
        if (rightNode == null) {
            return head.next;
        }

        while (rightNode.next != null) {
            rightNode = rightNode.next;
            leftNode = leftNode.next;
        }

        leftNode.next = leftNode.next.next;

        return head;
    }
}

class ListNode {
 int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
