
# [234. 回文列表](https://leetcode-cn.com/problems/palindrome-linked-list/)


## 想法


## 实现

```golang
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
