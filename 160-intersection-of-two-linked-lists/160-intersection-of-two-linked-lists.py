# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA,lenB = 0,0
        currA,currB = headA,headB
        while currA:
            currA = currA.next
            lenA+=1
        while currB:
            currB = currB.next
            lenB+=1
        diff = abs(lenB-lenA)
        longer,shorter = (headA,headB) if lenA>lenB else (headB,headA)
        for _ in range(diff):
            longer = longer.next
        while longer and shorter:
            if longer == shorter:
                return shorter
            longer = longer.next
            shorter = shorter.next
        return None