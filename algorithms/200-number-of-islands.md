# [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) - medium

<p>给你一个由 <code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## Solutions

### 1. DFS

使用 dp[i][j] 表示 grid[i][j] 是否访问过。遍历 grid 如果遇到陆地 `'1'`，则尝试标记这一整块陆地（DFS 递归标记上下左右位置）

时间复杂度 O(mn); 空间复杂度 O(mn)

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[False] * n for _ in range(m)]

        def mark(x, y):
            if x >= m or x < 0 or y >= n or y < 0 or grid[x][y] == '0' or dp[x][y]:
                return

            dp[x][y] = True

            mark(x - 1, y)
            mark(x + 1, y)
            mark(x, y - 1)
            mark(x, y + 1)

        ans = 0
        for i in range(m):
            for j, v in enumerate(grid[i]):
                if v == '0' or dp[i][j]:
                    continue
                ans += 1
                mark(i, j)

        return ans
```

可以直接修改 grid 避免 dp 开销

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def mark(x, y):
            if x >= m or x < 0 or y >= n or y < 0 or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            mark(x - 1, y)
            mark(x + 1, y)
            mark(x, y - 1)
            mark(x, y + 1)

        ans = 0
        for i in range(m):
            for j, v in enumerate(grid[i]):
                if v == '0':
                    continue
                ans += 1
                mark(i, j)

        return ans
```
