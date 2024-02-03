# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            # Extract values from each linked list, default to 0 if the list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            # Create a new node with the digit and link it to the result list
            current.next = ListNode(digit)
            current = current.next
            # Move to the next nodes in both linked lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next