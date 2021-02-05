# [496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/) - easy

<p>给你两个<strong> 没有重复元素</strong> 的数组 <code>nums1</code> 和 <code>nums2</code> ，其中<code>nums1</code> 是 <code>nums2</code> 的子集。</p>

<p>请你找出 <code>nums1</code> 中每个元素在 <code>nums2</code> 中的下一个比其大的值。</p>

<p><code>nums1</code> 中数字 <code>x</code> 的下一个更大元素是指 <code>x</code> 在 <code>nums2</code> 中对应位置的右边的第一个比 <code>x</code><strong> </strong>大的元素。如果不存在，对应位置输出 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2].
<strong>输出:</strong> [-1,3,-1]
<strong>解释:</strong>
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums1 = [2,4], nums2 = [1,2,3,4].
<strong>输出:</strong> [3,-1]
<strong>解释:</strong>
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums1.length <= nums2.length <= 1000</code></li>
	<li><code>0 <= nums1[i], nums2[i] <= 10<sup>4</sup></code></li>
	<li><code>nums1</code>和<code>nums2</code>中所有整数 <strong>互不相同</strong></li>
	<li><code>nums1</code> 中的所有整数同样出现在 <code>nums2</code> 中</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(nums1.length + nums2.length)</code> 的解决方案吗？</p>


## thinking

比较简单的思路是，先把 `nums2` 遍历一边，找到每一个数右边大于它的第一个数，存入一个 map 中。再把 `nums1` 遍历一遍，从 cache map 中取对应结果。没有取到为 `-1`。

这里有个优化的点，在第一次遍历的时候。使用“单调栈”可以提高遍历效率，将时间复杂度从 O(n^2) 降为 O(n)。

遍历 `nums2` 时，检查栈顶元素值，如果小于当前只，则当前值为栈顶值的“下一个大值”。循环检查栈顶，直到小于等于栈顶值：入栈。

## code

初始版本：
```golang
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	cache := make(map[int]int)
	size := len(nums2)
	for i, n := range nums2 {
		for j := i + 1; j < size; j++ {
			if nums2[j] > n {
				cache[n] = nums2[j]
				break
			}
		}
	}

	results := make([]int, len(nums1))
	for i, n := range nums1 {
		v, ok := cache[n]
		if !ok {
			v = -1
		}
		results[i] = v
	}
	return results
}

```

使用“单调栈”版本：
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        stack = []
        for i in nums2:
            if not stack or stack[-1] >= i:
                stack.append(i)
                continue
            while stack and stack[-1] < i:
                cache[stack.pop()] = i
            stack.append(i)

        return [cache.get(i, -1) for i in nums1]
```
