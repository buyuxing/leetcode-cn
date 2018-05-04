'''
https://leetcode-cn.com/problems/add-two-numbers/description/
2. 两数相加
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        head = p
        c = 0
        while l1 != None or l2 != None:
            sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + c
            c = sum // 10
            n = ListNode(sum % 10)
            p.next = n
            p = n
            if l1 !=None:
                l1 = l1.next
            if l2 !=None:
                l2 = l2.next 
      
        if c > 0:
            n = ListNode(1)
            p.next = n

        return head.next
import json
def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    l1 = stringToListNode("[1,2,4]")
    l2 = stringToListNode("[2,3,8]")
    r = addTwoNumbers(l1,l2)
    print(listNodeToString(r))

if __name__ == '__main__':
    main()