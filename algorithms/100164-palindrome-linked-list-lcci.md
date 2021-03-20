# [100164. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list-lcci/) - easy

<p>编写一个函数，检查输入的链表是否是回文的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入： </strong>1-&gt;2
<strong>输出：</strong> false 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入： </strong>1-&gt;2-&gt;2-&gt;1
<strong>输出：</strong> true 
</pre>

<p>&nbsp;</p>

<p><strong>进阶：</strong><br>
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？</p>


## thinking

### 1. 额外数组保存

最简单思路，讲链表保存到数组中，再使用双指针比较。使用 `O(n)` 空间复杂度，和 `O(n)` 时间复杂度。

### 2. 快慢指针反正链表

要达到 `O(1)` 空间复杂度，其实就是要将链表分为两部分，并将其中一部分原地**反转**。

## code


使用额外数组保存：
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        p = head
        while p:
            a.append(p.val)
            p = p.next
        l, r = 0, len(a) - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True
```

快慢指针寻找中间点，从中间往两头分别遍历:
```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        low, fast = head, head
        p = None
        while fast and fast.next:
            fast = fast.next.next
            n = low.next
            low.next = p
            p = low
            low = n

        if low is None:
            return True

        l, r = p, low
        if fast:
            # 奇数个, low 是中间节点
            r = r.next
        
        while p and r:
            if p.val != r.val:
                return False
            p = p.next
            r = r.next
        return p == r
```