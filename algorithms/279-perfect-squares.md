# [279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/) - medium

<p>给定正整数 <em>n</em>，找到若干个完全平方数（比如 <code>1, 4, 9, 16, ...</code>）使得它们的和等于<em> n</em>。你需要让组成和的完全平方数的个数最少。</p>

<p>给你一个整数 <code>n</code> ，返回和为 <code>n</code> 的完全平方数的 <strong>最少数量</strong> 。</p>

<p><strong>完全平方数</strong> 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，<code>1</code>、<code>4</code>、<code>9</code> 和 <code>16</code> 都是完全平方数，而 <code>3</code> 和 <code>11</code> 不是。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = <code>12</code>
<strong>输出：</strong>3 
<strong>解释：</strong><code>12 = 4 + 4 + 4</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = <code>13</code>
<strong>输出：</strong>2
<strong>解释：</strong><code>13 = 4 + 9</code></pre>
 

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>4</sup></code></li>
</ul>


## Solutions

### 1. 动态规划

用 dp[i] 记录和为 i 所需最小完全平方个数。状态转移 `dp[i] = min(dp[i], dp[i - v] + 1)`

时间复杂度为 O(n * m) m 表示小于 n 的完全平方个数，等于根号 n。
空间复杂度为 O(n + m)

```py
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        vs = []
        for i in range(n):
            v = i * i
            if v > n:
                break
            vs.append(v)
            dp[v] = 1
        
        for i in range(1, n + 1):
            for v in vs:
                if i <= v:
                    break
                dp[i] = min(dp[i], dp[i - v] + 1)
        
        return dp[-1]
```

优化版

```py
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        vs = [i * i for i in range(1, int(n ** 0.5) + 1)]

        for i in range(1, n + 1):
            for v in vs:
                if i < v:
                    break
                dp[i] = min(dp[i], dp[i - v] + 1)
        
        return dp[-1]
```

### 2. 贪心算法

递归计算 count 次获取到和为 n 是否可能。count 从小往大，当为 True 时返回 count

```py
class Solution:
    def numSquares(self, n: int) -> int:

        vs = [i * i for i in range(1, int(n ** 0.5) + 1)]

        def is_divided_by(n, count) -> bool:
            if count == 1:
                return n in vs
            
            for v in vs:
                if is_divided_by(n - v, count - 1):
                    return True
            return False
        
        for c in range(1, n + 1):
            if is_divided_by(n, c):
                return c
        return n
```


### 数学解法

当然自己想不出来。[题解](https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode/#%E6%96%B9%E6%B3%95%E4%BA%94%EF%BC%9A%E6%95%B0%E5%AD%A6%E8%BF%90%E7%AE%97)

数学证明，每个自然数都可以被表示为 4 个完全平方数的和（当 n 本身就是平方和时，表示为 n + 0^2 ... + 0^2）。当 `n != 4^k * (8 * m + 7)` 时，可以表示为 3 个平方和。

我们要求最小平方和个数。当 `n != 4^k * (8*m + 7)` 时，要一次判断是为本身为平方数和；是否为两个数平方和。

```py
class Solution:
    def numSquares(self, n: int) -> int:
    
        while n % 4 == 0:
            n //= 4
        
        if n % 8 == 7:
            return 4

        if self.is_sequares(n):
            return 1

        vs = [i * i for i in range(1, int(n ** 0.5) + 1)]
        for v in vs:
            if self.is_sequares(n - v):
                return 2

        return 3
        
        
    def is_sequares(self, n):
        v = int(n ** 0.5)
        return v * v == n

```
