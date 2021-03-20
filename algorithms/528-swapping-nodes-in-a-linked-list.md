# [528. 交换链表中的节点](https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list/) - medium

<p>给你链表的头节点 <code>head</code> 和一个整数 <code>k</code> 。</p>

<p><strong>交换</strong> 链表正数第 <code>k</code> 个节点和倒数第 <code>k</code> 个节点的值后，返回链表的头节点（链表 <strong>从 1 开始索引</strong>）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/10/linked1.jpg" style="width: 722px; height: 202px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[1,4,3,2,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [7,9,6,6,7,8,3,0,9,5], k = 5
<strong>输出：</strong>[7,9,6,6,8,7,3,0,9,5]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1], k = 1
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2], k = 1
<strong>输出：</strong>[2,1]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2,3], k = 2
<strong>输出：</strong>[1,2,3]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目是 <code>n</code></li>
	<li><code>1 <= k <= n <= 10<sup>5</sup></code></li>
	<li><code>0 <= Node.val <= 100</code></li>
</ul>


## thinking

### 1. 快慢指针

- 快指针先走 k 步，记录 k 节点值及其前节点值。
- 快慢指针一起走，直到快指针走到尾。慢指针就是倒数 k 个节点。同时记录其前一个值。
- 交换两个节点（注意当两个节点**相邻**时，交换的处理）

## code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        s = ListNode(next=head)
        low, fast = s, s
        pl, pf = None, None
        kn = None

        for i in range(k):
            pf, fast = fast, fast.next
        
        kn = fast

        while fast:
            fast = fast.next
            pl, low = low, low.next
        
        # swap kn and low
        if pl == kn:
            # pf, kn, low, others
            kn.next, low.next = low.next, kn
            pf.next = low
        elif pf == low:
            # pl, low, kn, others
            low.next, kn.next = kn.next, low
            pl.next = kn
        else:
            low.next, kn.next = kn.next, low.next
            pl.next, pf.next = pf.next, pl.next
        return s.next
```