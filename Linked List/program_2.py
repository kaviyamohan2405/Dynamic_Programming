'''
2. Reverse Linked List

Problem Statement:
Reverse a singly linked list.

Input Description:
- head: The head of a singly linked list.

Output Description:
- The head of the reversed linked list.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 5000
- -5000 <= Node.val <= 5000
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
3. Merge Two
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev and current one step forward
        current = next_node
    return prev

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
head = create_linked_list([1, 2, 3, 4, 5])
new_head = reverseList(head)
print(linked_list_to_list(new_head))  # Output: [5, 4, 3, 2, 1]

# Example 2
head = create_linked_list([1, 2])
new_head = reverseList(head)
print(linked_list_to_list(new_head))  # Output: [2, 1]

# Example 3
head = create_linked_list([])
new_head = reverseList(head)
print(linked_list_to_list(new_head))  # Output: []
