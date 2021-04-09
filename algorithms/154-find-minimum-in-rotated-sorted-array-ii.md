# [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) - hard

已知一个长度为 <code>n</code> 的数组，预先按照升序排列，经由 <code>1</code> 到 <code>n</code> 次 <strong>旋转</strong> 后，得到输入数组。例如，原数组 <code>nums = [0,1,4,4,5,6,7]</code> 在变化后可能得到：
<ul>
	<li>若旋转 <code>4</code> 次，则可以得到 <code>[4,5,6,7,0,1,4]</code></li>
	<li>若旋转 <code>7</code> 次，则可以得到 <code>[0,1,4,4,5,6,7]</code></li>
</ul>

<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> <strong>旋转一次</strong> 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。</p>

<p>给你一个可能存在 <strong>重复</strong> 元素值的数组 <code>nums</code> ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 <strong>最小元素</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,5]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,0,1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 5000</code></li>
	<li><code>-5000 <= nums[i] <= 5000</code></li>
	<li><code>nums</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<ul>
	<li>这道题是 <a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/">寻找旋转排序数组中的最小值</a> 的延伸题目。</li>
	<li>允许重复会影响算法的时间复杂度吗？会如何影响，为什么？</li>
</ul>


## Solutions

类似题目：
- [153. 寻找旋转排序数组中的最小值](./153-find-minimum-in-rotated-sorted-array.md)
- [81. 搜索旋转排序数组 II](./81-search-in-rotated-sorted-array-ii.md)

## 1. 暴力

直接找到连接点。

时间复杂度 O(n); 空间复杂度 O(1)

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0

        while p + 1 < n and nums[p] <= nums[p + 1]:
            p += 1

        return nums[0] if p == n - 1 else nums[p + 1]
```

## 2. 二分法

对半分为两半，因为相等缘故，没有办法区分哪组是有序的。如 a = [4, 5, 1, 4, 4, 4, 4]，没有办法区分在 `a[:3]` 还是在 `a[3:]`。
这时可以左右都往里走一位。变成 a = [5, 1, 4, 4, 4]

平均时间复杂度为 O(log n); 空间复杂度为 O(1)

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] == nums[m] and nums[r] == nums[m]:
                l += 1
                r -= 1
            elif nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]
```

题解中给出一个方案。在 [153. 寻找旋转排序数组中的最小值——2. 二分查找](./153-find-minimum-in-rotated-sorted-array.md#2-二分查找) 解法中增加一个分支，
如果 `nums[m] == nums[r]` 那就把 r 往左移动一位。

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1

        return nums[l]
```
