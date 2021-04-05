# [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/) - medium

<p>给定不同面额的硬币 <code>coins</code> 和一个总金额 <code>amount</code>。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 <code>-1</code>。</p>

<p>你可以认为每种硬币的数量是无限的。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>
<strong>输出：</strong><code>3</code> 
<strong>解释：</strong>11 = 5 + 5 + 1</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[2]</code>, amount = <code>3</code>
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>coins = [1], amount = 0
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>coins = [1], amount = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>coins = [1], amount = 2
<strong>输出：</strong>2
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= coins.length <= 12</code></li>
	<li><code>1 <= coins[i] <= 2<sup>31</sup> - 1</code></li>
	<li><code>0 <= amount <= 10<sup>4</sup></code></li>
</ul>


## Solutions

### 1. 暴力 + 缓存

设 f(n) 表示总和为 n 所需最少硬币数。直接暴力计算会超时。可以通过 cache 数组缓存 f(n) 结果。

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [0] * (amount + 1)

        def f(n: int) -> int:
            if n == 0:
                return 0
            elif n < 0:
                return -1

            if cache[n] != 0:
                return cache[n]

            i = -1
            for c in coins:
                 v = f(n - c)
                 if v >= 0 and (i == -1 or v < i):
                     i = v + 1
            cache[n] = i
            return i

        return f(amount)
```

### 2. 动态规划

用 `dp[i]` 表示和为 i 时，需要的最小硬币数。

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
```
