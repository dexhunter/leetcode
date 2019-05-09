class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        n2 = 0

        i = 1
        flag = True
        while flag:
            if l1.next is None:
                flag = False
            n1 += l1.val * i
            l1 = l1.next
            i = i * 10

        i = 1
        flag=True
        while flag:
            if l2.next is None:
                flag = False
            n2 += l2.val * i
            l2 = l2.next
            i = i * 10

        n = n1 + n2
        list_l = []
        for i in str(n):
            l = ListNode(int(i))
            list_l.append(l)

        for i in range(len(list_l)):
            if i == 0:
                list_l[i].next = None
            else:
                list_l[i].next = list_l[i-1]

        return list_l[-1]
