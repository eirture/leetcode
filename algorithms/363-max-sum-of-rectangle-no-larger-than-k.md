# [363. 矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/) - hard

<p>给你一个 <code>m x n</code> 的矩阵 <code>matrix</code> 和一个整数 <code>k</code> ，找出并返回矩阵内部矩形区域的不超过 <code>k</code> 的最大数值和。</p>

<p>题目数据保证总会存在一个数值和不超过 <code>k</code> 的矩形区域。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg" style="width: 255px; height: 176px;" />
<pre>
<strong>输入：</strong>matrix = [[1,0,1],[0,-2,3]], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>蓝色边框圈出来的矩形区域 <code>[[0, 1], [-2, 3]]</code> 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[2,2,-1]], k = 3
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>-100 <= matrix[i][j] <= 100</code></li>
	<li><code>-10<sup>5</sup> <= k <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>如果行数远大于列数，该如何设计解决方案？</p>


## Solutions

### 1. 前缀和

（看到区间求和问题，想一想前缀和！）

这题比较复杂，求一个矩阵和最接近 k。矩阵的和由每一列和每一行决定。我们假设只有一行。那这个问题就简化为数组区间和问题。

我们固定行，将 matrix[i:j + 1] 每一列求和，得 row。对 row 求前缀和。在迭代 row 求和时，使用有序数组存储前缀和，并尝试求最大小于等于 `s - k` 的前缀和。则有 `ans = max(ans, s - sorted_list[x])`。如果 `ans == k` 其实就可以返回结果了。

参考题解，使用了 `sortedcontainers` 中的 `SortedList` 数据结构。

```py
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            row = [0] * n
            for j in range(i, m):
                for c in range(n):
                    row[c] += matrix[j][c]

                s = 0
                sorted_list = SortedList([0])
                for v in row:
                    s += v
                    x = sorted_list.bisect_left(s - k)
                    if x != len(sorted_list):
                        ans = max(ans, s - sorted_list[x])
                        # we can return if ans == k
                        if ans == k:
                            return k
                    sorted_list.add(s)

        return ans
```
