# [494. 目标和](https://leetcode-cn.com/problems/target-sum/) - medium

<p>给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号&nbsp;<code>+</code>&nbsp;和&nbsp;<code>-</code>。对于数组中的任意一个整数，你都可以从&nbsp;<code>+</code>&nbsp;或&nbsp;<code>-</code>中选择一个符号添加在前面。</p>

<p>返回可以使最终数组和为目标数 S 的所有添加符号的方法数。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>nums: [1, 1, 1, 1, 1], S: 3
<strong>输出：</strong>5
<strong>解释：</strong>

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>数组非空，且长度不会超过 20 。</li>
	<li>初始的数组的和不会超过 1000 。</li>
	<li>保证返回的最终结果能被 32 位整数存下。</li>
</ul>


## Solutions

### 1. 递归调用

最容易想到递归

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 1:
            v = 2 if S == 0 else 1
            return v if abs(nums[0]) == abs(S) else 0
        
        n1 = self.findTargetSumWays(nums[1:], S - nums[0])
        n2 = self.findTargetSumWays(nums[1:], S + nums[0])
        return n1 + n2
```

python 运行超时 :-(，用 go 写一遍 OK

```go
func findTargetSumWays(nums []int, S int) int {
    if len(nums) == 1 {
        switch {
        case S == 0 && nums[0] == 0:
            return 2
        case nums[0] == S || nums[0] == -S:
            return 1
        default:
            return 0
        }
    }

    return findTargetSumWays(nums[1:], S - nums[0]) + findTargetSumWays(nums[1:], S + nums[0])
}
```


### 2. 动态规划

动态规划的思路是，把第 i 位所有可能的和的个数都算一遍。

dp[i][sum + nums[i]] += dp[i][sum] 
dp[i][sum - nums[i]] += dp[i][sum]

最终的结果就是 `dp[len(nums) - 1][S]`


```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [[0] * 2001 for _ in nums]
        dp[0][nums[0]] = 1
        dp[0][-nums[0]] += 1

        i = 1
        while i < len(nums):
            for s in range(-1000, 1001):
                if dp[i - 1][s] == 0:
                    continue
                dp[i][s + nums[i]] += dp[i - 1][s]
                dp[i][s - nums[i]] += dp[i - 1][s]
            i += 1

        if S > 1000:
            return 0
        return dp[len(nums) - 1][S]
```
