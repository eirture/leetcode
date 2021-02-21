# [234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/) - easy

<p>请判断一个链表是否为回文链表。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 1-&gt;2
<strong>输出:</strong> false</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 1-&gt;2-&gt;2-&gt;1
<strong>输出:</strong> true
</pre>

<p><strong>进阶：</strong><br>
你能否用&nbsp;O(n) 时间复杂度和 O(1) 空间复杂度解决此题？</p>


## thinking

## code

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    var fast, slow, pre *ListNode = head, head, nil

	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next

		next := slow.Next

		slow.Next = pre
		pre = slow
		slow = next
	}

	if fast != nil {
		slow = slow.Next
	}

	for slow != nil {
		if pre.Val != slow.Val {
			return false
		}
		slow = slow.Next
		pre = pre.Next
	}

	return true
}
```
