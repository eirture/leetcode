# [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) - medium

<p>给定一个整数数组，其中第<em>&nbsp;i</em>&nbsp;个元素代表了第&nbsp;<em>i</em>&nbsp;天的股票价格 。​</p>

<p>设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:</p>

<ul>
	<li>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</li>
	<li>卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。</li>
</ul>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,2,3,0,2]
<strong>输出: </strong>3 
<strong>解释:</strong> 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]</pre>


## Solutions

### 1. 动态规划

类似题目：
- [121. 买卖股票的最佳时机](./121-best-time-to-buy-and-sell-stock.md)
- [122. 买卖股票的最佳时机 II](./122-best-time-to-buy-and-sell-stock-ii.md)
- [123. 买卖股票的最佳时机 III](./123-best-time-to-buy-and-sell-stock-iii.md)
- [188. 买卖股票的最佳时机 IV](./188-best-time-to-buy-and-sell-stock-iv.md)

第 i 天有三种状态：

0. 持有股票。最大收益记为 `f[i][0]`
1. 不持有股票，且处于冷冻期。最大收益记为 `f[i][1]`
2. 不持有股票，且不处于冷冻期。最大收益记为 `f[i][2]`

对应状态转移如下：
- f[i][0]，两种情况：前一天持有一支股票 `f[i - 1]`；前一天处于 `2` 且当天买了一支股票 `f[i - 1][2] - prices[i]`
- f[i][1]，只有一种情况：当天卖出了股票（前一天只能为 f[i - 1][0]） `f[i - 1][0] + prices[i]`
- f[i][2]，两种情况：前一天不持有股票且处于冷冻期 `f[i - 1][1]`；前一天不持有股票且不处于冷冻期 `f[i - 1][2]`

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0

        for p in prices:
            f0, f1, f2 = max(f0, f2 - p), f0 + p, max(f1, f2)
        
        return max(f1, f2)
```
