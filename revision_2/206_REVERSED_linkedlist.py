"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_ll_recursively(head):
    tail = None
    return foo(head, tail)

def foo(head, tail):
    if head == None:
        return tail
    else:
        save = head.next
        head.next = tail
        tail = head
        head = save
        return foo(head, tail)



def reverse_ll_iteratively(head):

    tail = None
    while head:
        save = head.next
        head.next = tail
        tail = head
        head = save

    return tail

