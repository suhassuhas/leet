# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seenA = set()
        seenB = set()
        while headA or headB:
            if headA:
                if headA in seenB:
                    return headA
                seenA.add(headA)
                headA = headA.next
            if headB:
                if headB in seenA:
                    return headB
                seenB.add(headB)
                headB = headB.next
        return None
            