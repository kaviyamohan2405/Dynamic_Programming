'''
1. Remove Nth Node From End of List

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input Description:
- head: The head of a singly linked list.
- n: An integer representing the position from the end of the list.

Output Description:
- The head of the modified linked list.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The second node from the end is 4, so we remove it.

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: The first node from the end is 1, so we remove it.

Example 3:
Input: head = [1,2], n = 1
Output: [1]
Explanation: The second node from the end is 2, so we remove it.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move first to the end, maintaining the gap
    while first is not None:
        first = first.next
        second = second.next

    # Skip the desired node
    second.next = second.next.next

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode(0)
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

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
n = 2
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 5]

head = create_linked_list([1])
n = 1
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # Output: []

head = create_linked_list([1, 2])
n = 1
new_head = removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # Output: [1]
