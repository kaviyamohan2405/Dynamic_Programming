'''
3. Merge Two Sorted Lists

Problem Statement:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing
together the nodes of the first two lists.

Input Description:
- list1: The head of the first sorted linked list.
- list2: The head of the second sorted linked list.

Output Description:
- The head of the merged sorted linked list.

Constraints:
- The number of nodes in both lists is sz.
- 0 <= sz <= 50
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Append the remaining nodes from either list1 or list2
    tail.next = list1 if list1 else list2

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
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
new_head = mergeTwoLists(list1, list2)
print(linked_list_to_list(new_head))  # Output: [1, 1, 2, 3, 4, 4]

# Example 2
list1 = create_linked_list([])
list2 = create_linked_list([])
new_head = mergeTwoLists(list1, list2)
print(linked_list_to_list(new_head))  # Output: []

# Example 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
new_head = mergeTwoLists(list1, list2)
print(linked_list_to_list(new_head))  # Output: [0]
