'''
5. Add Two Numbers

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers
and return the sum as a linked list.

Input Description:
- l1: The head of the first linked list.
- l2: The head of the second linked list.

Output Description:
- The head of the linked list representing the sum of the two numbers.

Constraints:
- The number of nodes in each linked list is sz.
- 1 <= sz <= 100
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1 + val2 + carry, 10)
        
        current.next = ListNode(out)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example usage:
# Example 1
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result_head = addTwoNumbers(l1, l2)
print(linked_list_to_list(result_head))  # Output: [7, 0, 8]

# Example 2
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result_head = addTwoNumbers(l1, l2)
print(linked_list_to_list(result_head))  # Output: [0]

# Example 3
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result_head = addTwoNumbers(l1, l2)
print(linked_list_to_list(result_head))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
