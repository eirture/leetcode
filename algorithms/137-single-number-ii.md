# [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/) - medium

<p>给你一个整数数组 <code>nums</code> ，除某个元素仅出现 <strong>一次</strong> 外，其余每个元素都恰出现 <strong>三次 。</strong>请你找出并返回那个只出现了一次的元素。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,3,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0,1,0,1,99]
<strong>输出：</strong>99
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code></li>
	<li><code>nums</code> 中，除某个元素仅出现 <strong>一次</strong> 外，其余每个元素都恰出现 <strong>三次</strong></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>


## Solutions

### 1. 排序遍历

先排序，然后每步 3 个做遍历

时间复杂度取决于排序取 O(n * log n), 空间复杂度 O(1)

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        i = 0
        while i + 2 < n:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3
        
        return nums[-1]
```

### 2. hash map

通过 map 统计数据个数，出现次数为 3 则丢弃，最终只剩下出现次数为 1 的值

时间复杂度为 O(n), 空间复杂度 O(n)

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            c = m.pop(n, 0)
            c += 1
            if c == 3:
                continue
            m[n] = c

        i, _ = m.popitem()
        return i
```
