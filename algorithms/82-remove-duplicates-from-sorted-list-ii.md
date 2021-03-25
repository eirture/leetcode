# [82. 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/) - medium

<p>存在一个按升序排列的链表，给你这个链表的头节点 <code>head</code> ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 <strong>没有重复出现</strong><em> </em>的数字。</p>

<p>返回同样按升序排列的结果链表。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,3,4,4,5]
<strong>输出：</strong>[1,2,5]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="width: 500px; height: 205px;" />
<pre>
<strong>输入：</strong>head = [1,1,1,2,3]
<strong>输出：</strong>[2,3]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目在范围 <code>[0, 300]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
	<li>题目数据保证链表已经按升序排列</li>
</ul>


## Solutions

### 1. 使用迭代思路

pre, l, r 三个指针，r 往后走，如果 `r.val != l.val` 有两种情况：r = l.next 说明没有重复，pre = l, l = r (l.next); 
r != l.next 说明有重复，此时 r 已经跳过重复的对象，pre.next = r, l = r。继续判断。直到 `r is None` 这应该当作 `r.val != l.val` 处理。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = ListNode(0, head)
        pre, l, r = s, head, head

        while r:
            r = r.next
            if not r or r.val != l.val:
                if l.next == r:
                    pre = l
                else:
                    pre.next = r
                l = r
        return s.next
```

官方题解也适用迭代思路，不过代码更简洁：

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        s = ListNode(101, head)
        p = s

        while p and p.next and p.next.next:
            if p.next.val == p.next.next.val:
                v = p.next.val
                while p.next and p.next.val == v:
                    p.next = p.next.next
            else:
                p = p.next
        return s.next
```

### 2. 使用递归思路

判断当前节点是否等于下一个节点，如果不相等。当前节点保留，next 值从递归调用中来。如果相等，一直找到不相等的节点 p。直接返回递归 p 的值。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return head
        
        p = head.next
        while p and p.val == head.val:
            p = p.next

        if head.next == p:
            # 保留当前节点
            head.next = self.deleteDuplicates(p)
            return head
        else:
            # 删除当前节点
            return self.deleteDuplicates(p)
```