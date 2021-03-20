# [100168. 环路检测](https://leetcode-cn.com/problems/linked-list-cycle-lcci/) - medium

<p>给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。</p>

<p>如果链表中有某个节点，可以通过连续跟踪 <code>next</code> 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 <code>pos</code> 是 <code>-1</code>，则在该链表中没有环。<strong>注意：<code>pos</code> 不作为参数进行传递</strong>，仅仅是为了标识链表的实际情况。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" style="height: 97px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>head = [3,2,0,-4], pos = 1
<strong>输出：</strong>tail connects to node index 1
<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 74px; width: 141px;" /></p>

<pre>
<strong>输入：</strong>head = [1,2], pos = 0
<strong>输出：</strong>tail connects to node index 0
<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 45px; width: 45px;" /></p>

<pre>
<strong>输入：</strong>head = [1], pos = -1
<strong>输出：</strong>no cycle
<strong>解释：</strong>链表中没有环。</pre>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你是否可以不用额外空间解决此题？</li>
</ul>

<p> </p>


## thinking

#### 初级想法
使用集合记录所有走过的 Node

#### 快慢指针
快指针每次走 1 步，快指针每次走 2 步。如果有环，一定会相遇。

遇到的问题：
- 相遇点不是环的入口点，怎么找到环的环点？

最开始想法时，确认有环以后，再用两个指针遍历。i 从 head 开始，f 从相遇点开始。如果 `i == f` 此时为环点。如果 f 重新走到相遇点。则此时 i 还在环外，`i = i.next`，继续直到找到环点。

#### 题解

官方题解中也只有集合记录，和快慢指针。

快慢指针检测到环以后，数学证明，“相遇点”到“环点”距离正好等于“头”到“相遇点”距离。

![](https://pic.eirture.cn/pics/jindian_02.08.png)

快指针走过的距离永远是慢指针的 2 倍。假设快指针走了 n 圈。有 `a + n(b + x) + b = 2(a + b)`
推导 `(n-1) * (b + c) - c = a`。

所以，在检测到有环时，从链表头和相遇点同时往后走，直到两个指针相遇，就是“环点”。

## code

集合记录经过的节点：
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pn = []
        n = head
        while n:
            if n in pn:
                return n
            pn.append(n)
            n = n.next
        return None
            
```

使用快慢指针检测为环后，使用遍历法找到“环点”。

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        l, f = head, head
        while True:
            if not f or not f.next:
                return None
            f = f.next.next
            if f == l:
                break
            l = l.next
        # have cycle
        i = head
        while i != l:
            n = l.next
            while n != l:
                if n == i:
                    return i
                n = n.next
            i = i.next
        return i

```

相遇点到环点距离正好等于链表头到相遇点的距离：

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        l, f = head, head
        while f:
            l = l.next
            if not f.next:
                return None
            f = f.next.next
            if f == l:
                i = head
                while i != l:
                    i = i.next
                    l = l.next
                return i

        return None
        
```
