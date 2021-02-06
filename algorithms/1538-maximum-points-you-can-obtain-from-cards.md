# [1538. 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/) - medium

<p>几张卡牌<strong> 排成一行</strong>，每张卡牌都有一个对应的点数。点数由整数数组 <code>cardPoints</code> 给出。</p>

<p>每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 <code>k</code> 张卡牌。</p>

<p>你的点数就是你拿到手中的所有卡牌的点数之和。</p>

<p>给你一个整数数组 <code>cardPoints</code> 和整数 <code>k</code>，请你返回可以获得的最大点数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>输出：</strong>12
<strong>解释：</strong>第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cardPoints = [2,2,2], k = 2
<strong>输出：</strong>4
<strong>解释：</strong>无论你拿起哪两张卡牌，可获得的点数总是 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>输出：</strong>55
<strong>解释：</strong>你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,1000,1], k = 1
<strong>输出：</strong>1
<strong>解释：</strong>你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,79,80,1,1,1,200,1], k = 3
<strong>输出：</strong>202
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cardPoints.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= cardPoints[i] &lt;= 10^4</code></li>
	<li><code>1 &lt;= k &lt;= cardPoints.length</code></li>
</ul>


## thinking

这个题目的关键在于明白，**选的卡片是连续的，前面 `n` 张，后面 `k-n` 张**。然后找到和的最大值。

## code

一开始觉得这是一个动态规划，DFS 超时。

```python
class Solution:
    def __init__(self):
        self.v = 0

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        self.f(cardPoints, k, 0)
        return self.v
    
    def f(self, a: List[int], k: int, v: int):
        if v > self.v:
            self.v = v
        
        if k == 0:
            return
        
        self.f(a[1:], k-1, v+a[0])
        self.f(a[:-1], k-1, v+a[-1])
```

看了题解思路分分钟写出来，害。

```go
func maxScore(cardPoints []int, k int) int {
    lSum := 0
    rSum := 0
    size := len(cardPoints)
    for i := 1; i <= k; i++ {
        rSum += cardPoints[size-i]
    }
    v := rSum
    idx := size - k
    for i := 0; i < k; i++ {
        lSum += cardPoints[i]
        rSum -= cardPoints[idx+i]
        if lSum + rSum > v {
            v = lSum + rSum
        }
    }
    return v
}
```