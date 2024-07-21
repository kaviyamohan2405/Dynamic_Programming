'''
4. Linked List Cycle

Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Input Description:
- head: The head of a singly linked list.

Output Description:
- true if there is a cycle in the linked list, otherwise false.

Constraints:
- The number of nodes in the list is sz.
- 0 <= sz <= 10^4
- -10^5 <= Node.val <= 10^5

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node
(0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    dummy = ListNode()
    current = dummy
    cycle_node = None

    for index, value in enumerate(values):
        current.next = ListNode(value)
        current = current.next
        if index == pos:
            cycle_node = current

    if cycle_node:
        current.next = cycle_node

    return dummy.next

# Example usage:
# Example 1
head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
print(hasCycle(head))  # Output: True

# Example 2
head = create_linked_list_with_cycle([1, 2], 0)
print(hasCycle(head))  # Output: True

# Example 3
head = create_linked_list_with_cycle([1], -1)
print(hasCycle(head))  # Output: False
