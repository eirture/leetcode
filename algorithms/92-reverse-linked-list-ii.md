# [92. 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii/) - medium

给你单链表的头指针 <code>head</code> 和两个整数 <code>left</code> 和 <code>right</code> ，其中 <code>left <= right</code> 。请你反转从位置 <code>left</code> 到位置 <code>right</code> 的链表节点，返回 <strong>反转后的链表</strong> 。
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], left = 2, right = 4
<strong>输出：</strong>[1,4,3,2,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [5], left = 1, right = 1
<strong>输出：</strong>[5]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目为 <code>n</code></li>
	<li><code>1 <= n <= 500</code></li>
	<li><code>-500 <= Node.val <= 500</code></li>
	<li><code>1 <= left <= right <= n</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong> 你可以使用一趟扫描完成反转吗？</p>


## thinking

### 1. 原地反转

使用单指针，先走到 left 位置，记录 pre 位置 l，继续往下走到 right 位置，并原地反转链表。最后交换反转后的链表拼接到原来位置。

空间复杂度：O(1), 时间复杂度：O(n)

### 2. 官方题解

官方题解有个类似方案，但是它并不是“反转链表”，而是往前插入。（本质上也是反转，更好理解一些）

## code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h = ListNode(next=head)
        p = h
        pre = None
        i = 0
        while i < left:
            pre, p = p, p.next
            i += 1
        l = pre
        
        # 注意此处边界
        while i <= right:
            i += 1
            next = p.next

            p.next, pre = pre, p
            p = next
        
        l.next.next = p
        l.next = pre
        return h.next

```

官方题解思路：
```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        s = ListNode(next=head)
        pre = s
        for i in range(left - 1):
            pre = pre.next
        
        cur = pre.next
        for i in range(right-left):
            next = cur.next

            # 此处 cur 永远都是 left 位置上的那个元素，每次迭代都会修改 cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        
        return s.next
```
