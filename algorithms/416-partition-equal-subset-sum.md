# [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/) - medium

<p>给定一个<strong>只包含正整数</strong>的<strong>非空</strong>数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。</p>

<p><strong>注意:</strong></p>

<ol>
	<li>每个数组中的元素不会超过 100</li>
	<li>数组的大小不会超过 200</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2:</strong></p>

<pre>输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
</pre>

<p>&nbsp;</p>


## Solutions

### 动态规划

看了题解，巧妙。

这个问题等价于 从 nums 中取 k 个数，使它的和等于 `sum(nums) / 2`。

如果数据的长度 n <= 1，那一定不能分为两个和相等的数组。如果 `sum(nums)` 是个奇数，也一定不能分。如果 `max(nums) > sum(nums)/2`，不能分。

用二维数组 dp[i][j] 记录取 i 个数和为 j 是否可以。那么 `0 <= i < len(nums)`，`0 <= j <= sum(nums)/2`。且 dp[i][0] 都是可以的。因为只要都不取。

初始化，`dp[0][nums[0]] = True`。i 从 1 开始，有两种可能。`nums[i] <= j`，那么 i 这个数可以取，也可以不取。对应 `dp[i - 1][j]` or `dp[i - 1][j - nums[i]]`。如果 `nums[i] > j`，i 这个数一定不能取。对应 `dp[i - 1][j]`。

最终 `dp[n-1][target]` 就是结果。

空间复杂度为 O(n * target)，时间复杂度为 O(n * target)

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        total = sum(nums)
        maxv = max(nums)
        
        if total % 2:
            return False
        
        target = total // 2
        if maxv > target:
            return False
        
        dp = [[True] + [False] * target for _ in nums]
        dp[0][nums[0]] = True
        for i in range(1, n):
            v = nums[i]
            for j in range(1, target + 1):
                if j >= v:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - v]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
```

这里 i 每次迭代，都只与上一行有关，dp 只需要一维就行。但是需要从右往左遍历。如果从左往右计算 `dp[j] ｜= dp[j - v]` 时，`dp[j - v]` 已经被更新，不是上一行的值了。

空间复杂度降为 O(n)

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        total = sum(nums)
        maxv = max(nums)
        
        if total % 2:
            return False
        target = total // 2
        if maxv > target:
            return False
        
        dp = [True] + [False] * target
        for i, v in enumerate(nums):
            for j in range(target, v - 1, -1):
                dp[j] |= dp[j - v]
            
        return dp[-1]
```
