# [213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/) - medium

<p>你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 <strong>围成一圈</strong> ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong> 。</p>

<p>给定一个代表每个房屋存放金额的非负整数数组，计算你 <strong>在不触动警报装置的情况下</strong> ，能够偷窃到的最高金额。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,2]
<strong>输出：</strong>3
<strong>解释：</strong>你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1]
<strong>输出：</strong>4
<strong>解释：</strong>你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 1000</code></li>
</ul>


## Solutions

类似于： [198. 打家劫舍](./198-house-robber.md)

### 1. 动态规划

跟 [198. 打家劫舍](./198-house-robber.md) 有点不同的是，前后不能同时偷。在迭代的时候，同时计算 `nums[0:n]`, `nums[0:n - 1]`, `nums[1:n]` 三种情况。

如果 nums[0:n] 对应的 v2 >= v1, 说明最后一家不偷，直接返回 v2；
否则返回其他里面最大的。

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        v1, v2 = nums[0], 0
        x1, x2 = 0, 0
        z1, z2 = 0, 0
        for i in range(1, n):
            z1, z2 = v1, v2
            v1, v2 = v2 + nums[i], max(v1, v2)
            x1, x2 = x2 + nums[i], max(x1, x2)
        
        if v2 >= v1:
            return v2
        
        return max(z1, z2, x1, x2)
```
