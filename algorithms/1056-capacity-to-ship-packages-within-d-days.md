# [1056. 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/) - medium

<p>传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。</p>

<p>传送带上的第 <code>i</code>&nbsp;个包裹的重量为&nbsp;<code>weights[i]</code>。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。</p>

<p>返回能在 <code>D</code> 天内将传送带上的所有包裹送达的船的最低运载能力。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>weights = [1,2,3,4,5,6,7,8,9,10], D = 5
<strong>输出：</strong>15
<strong>解释：</strong>
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>weights = [3,2,2,4,1,4], D = 3
<strong>输出：</strong>6
<strong>解释：</strong>
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>weights = [1,2,3,1,1], D = 4
<strong>输出：</strong>3
<strong>解释：</strong>
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= D &lt;= weights.length &lt;= 50000</code></li>
	<li><code>1 &lt;= weights[i] &lt;= 500</code></li>
</ol>


## Solutions

### 1. 暴力

从 max(weights) 开始，判断运载能力如果是当前值，是否可以在 D 天内运送完成。

```py
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        psums = [0] * (n + 1)
        x = 0
        for i, w in enumerate(weights):
            x = max(x, w)
            psums[i + 1] = psums[i] + w
        
        dp = [0] * (D + 1)
        d = 0

        while True:
            i, j = dp[d], dp[d + 1]
            while j < n and psums[j + 1] - psums[i] <= x:
                j += 1

            dp[d + 1] = j
            if j == n:
                break

            d += 1
            if d == D:
                x += 1
                d = 0
        
        return x
```

超时

### 2. 二分查找

要求的最终结果在 `max(weights) - sum(weights)` 之间，使用二分查找，判断每次二分点是不是满足 D 天可以将所有包裹送达。在可以送达的承载能力集合中，找到最小值。

```py
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2

            d, sw = 1, 0
            for w in weights:
                if sw + w > m:
                    d += 1
                    sw = 0
                sw += w
            
            if d <= D:
                r = m
            else:
                l = m + 1

        return l
```
