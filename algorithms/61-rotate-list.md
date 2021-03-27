# [61. 旋转链表](https://leetcode-cn.com/problems/rotate-list/) - medium

<p>给你一个链表的头节点 <code>head</code> ，旋转链表，将链表每个节点向右移动 <code>k</code><em> </em>个位置。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 600px; height: 254px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[4,5,1,2,3]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 472px; height: 542px;" />
<pre>
<strong>输入：</strong>head = [0,1,2], k = 4
<strong>输出：</strong>[2,0,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 500]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
	<li><code>0 <= k <= 2 * 10<sup>9</sup></code></li>
</ul>


## Solutions

先走到链表最后一位 `p`, 将链表末尾指向 head，同时计算链表长度。旋转 k 次，就是倒数第 k 作为链表头，重新断开，并返回链表头。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        n = 1
        p = head
        while p.next:
            p = p.next
            n += 1

        p.next = head
        v = k % n
        while n > v:
            p = p.next
            n -= 1
        h = p.next
        p.next = None
        return h
```

