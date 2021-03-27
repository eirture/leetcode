# [581. 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/) - medium

<p>给你一个整数数组 <code>nums</code> ，你需要找出一个 <strong>连续子数组</strong> ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。</p>

<p>请你找出符合题意的 <strong>最短</strong> 子数组，并输出它的长度。</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,6,4,8,10,9,15]
<strong>输出：</strong>5
<strong>解释：</strong>你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n)</code> 的解决方案吗？</p>
</div>
</div>


## Solutions

### 1. 排序 + 比较

这个复杂度在于排序，排序后的比较复杂度在 O(n),

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        l = 0
        while l < len(nums) and s[l] == nums[l]:
            l += 1
        if l == len(nums):
            return 0

        r = len(nums) - 1
        while r >= 0 and s[r] == nums[r]:
            r -= 1
        return r - l + 1
```

### 2. 使用栈

从左往右遍历，寻找左边界 `l`。使用栈记录保存过的 index，如果当前值小于栈顶元素，则弹出栈顶元素，并记录最小 idx，即为左边界。
同理从右往左遍历，找到右边界 `r`。如果 `r` <= `l`，则说明已经有序。否则就是 `r - l + 1`。

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = []
        l, r = len(nums), 0
        
        i = 0
        while i < len(nums):
            while a and nums[a[-1]] > nums[i]:
                l = min(l, a.pop())
            a.append(i)
            i += 1
        
        del a[:]
        j = len(nums) - 1
        while j >= 0:
            while a and nums[a[-1]] < nums[j]:
                r = max(r, a.pop())
            a.append(j)
            j -= 1
        
        return 0 if r <= l else r - l + 1
```