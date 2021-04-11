# [264. 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/) - medium

<p>给你一个整数 <code>n</code> ，请你找出并返回第 <code>n</code> 个 <strong>丑数</strong> 。</p>

<p><strong>丑数 </strong>就是只包含质因数 <code>2</code>、<code>3</code> 和/或 <code>5</code> 的正整数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10
<strong>输出：</strong>12
<strong>解释：</strong>[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>1 通常被视为丑数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 1690</code></li>
</ul>


## Solutions

### 1. 动态规划

使用 dp[i] 表示第 i 个丑数，用 p1, p2, p3 维护三个指针，分别用于计算乘于 2, 3, 5 的值 n1, n2, n3。对应最小值就为 dp[i]，且更新对应最小值 p 指针。为了避免重复，要检查所有 p。如 dp[p1] = 3, dp[p2] = 2 时，`dp[p1] * 2` 和 `dp[p2] * 3` 会有相同结果。

```py
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p1 = p2 = p3 = 1

        for i in range(2, n + 1):
            n1, n2, n3 = dp[p1] * 2, dp[p2] * 3, dp[p3] * 5
            dp[i] = min(n1, n2, n3)
            if n1 == dp[i]:
                p1 += 1
            if n2 == dp[i]:
                p2 += 1
            if n3 == dp[i]:
                p3 += 1
        
        return dp[-1]
```
