# [368. 最大整除子集](https://leetcode-cn.com/problems/largest-divisible-subset/) - medium

给你一个由 <strong>无重复</strong> 正整数组成的集合 <code>nums</code> ，请你找出并返回其中最大的整除子集 <code>answer</code> ，子集中每一元素对 <code>(answer[i], answer[j])</code> 都应当满足：
<ul>
	<li><code>answer[i] % answer[j] == 0</code> ，或</li>
	<li><code>answer[j] % answer[i] == 0</code></li>
</ul>

<p>如果存在多个有效解子集，返回其中任何一个均可。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>[1,3] 也会被视为正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,8]
<strong>输出：</strong>[1,2,4,8]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 2 * 10<sup>9</sup></code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>


## Solutions

### 1. 动态规划

首先我们让数组有序

使用 dp[i] 表示以 nums[i] 为最大值时，整除子集的长度。初始值都为 1。我们遍历 `0 <= j < i` 当 `nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]` 时，更新 `dp[i]` 的值为 `dp[j] + 1`。同时记录 dp[i] 的最大值 maxs。

当拿到 dp 数组时，我们再找到 `dp[x] == maxs` 然后找到 `dp[z] == maxs - 1`，以此类推。直到 maxs == 0，就得到了最大整除子集。

时间复杂度 O(n^2); 空间复杂度 O(n)

```py
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        maxs = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            maxs = max(maxs, dp[i])
        
        ans = []
        for i in range(n - 1, -1, -1):
            if dp[i] == maxs and (not ans or ans[-1] % nums[i] == 0):
                ans.append(nums[i])
                maxs -= 1

        return ans
```
