# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li_total = []
        n = len(lists)
        for i in range(n):
            head = lists[i]
            while head:
                li_total.append(head.val)
                head = head.next
        li_total.sort()
        res = ListNode(0)
        cur = res
        for i in li_total:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next