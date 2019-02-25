class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def get_intersection_node(headA, headB):
    """Runtime: 204 ms, faster than 78.90% of Python online submissions for Intersection
     of Two Linked Lists."""

     """ Steps:
     1. Count the extra nodes for the longer LL, either diffA or diffB
     2. If diffA or diffB is zero means LLA or LLB is shorter respectively
     3. Therefore just step either diffA on LLA or step diffB on LLB
     4. At last start steping both LLA and LLB while comparing their nodes
     5. When there is a match of the nodes, you got it man!!!!
     """

    diffA, diffB = 0, 0
    heada, headb = headA, headB
    while heada or headb:

        if not heada:
            diffB += 1
        if not headb:
            diffA += 1
        if heada:
            heada = heada.next
        if headb:
            headb = headb.next

    if diffA:
        for _ in range(diffA):
            headA = headA.next
    if diffB:
        for _ in range(diffB):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA.val
        headA = headA.next
        headB = headB.next

common = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, common))
headB = ListNode(5, ListNode(0, ListNode(1, common)))
print(get_intersection_node(headA, headB))
