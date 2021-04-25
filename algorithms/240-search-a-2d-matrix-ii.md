# [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/) - medium

<p>编写一个高效的算法来搜索 <code><em>m</em> x <em>n</em></code> 矩阵 <code>matrix</code> 中的一个目标值 <code>target</code> 。该矩阵具有以下特性：</p>

<ul>
	<li>每行的元素从左到右升序排列。</li>
	<li>每列的元素从上到下升序排列。</li>
</ul>

<p> </p>

<p><b>示例 1：</b></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<b>输出：</b>true
</pre>

<p><b>示例 2：</b></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<b>输出：</b>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= n, m <= 300</code></li>
	<li><code>-10<sup>9</sup> <= matix[i][j] <= 10<sup>9</sup></code></li>
	<li>每行的所有元素从左到右升序排列</li>
	<li>每列的所有元素从上到下升序排列</li>
	<li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>
</ul>


## Solutions

### 1. 遍历

逐层遍历，由于 matrix 的特性，可以记录上一次遍历的最后一位 index，下面的行，对应 index 上的值也一定大于 target。所以后面都不用遍历。

最坏情况 target 大于 matrix 中所有数据，时间复杂度 O(m*n)；空间复杂度 O(1)

```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = 0
        x = n
 
        while i < m:
            j = 0
            while j < x:
                v = matrix[i][j] 
                if v == target:
                    return True
                elif v > target:
                    x = j
                    if x == 0:
                        return False
                    break
                j += 1
            i += 1

        return False
```

可以优化一下，将每一行的查找改为二分查找

```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = 0
        
        r = n - 1
        while i < m:
            l = 0
            while l <= r:
                p = (l + r) // 2
                v = matrix[i][p] 
                if v == target:
                    return True
                elif v > target:
                    r = p - 1
                else:
                    l = p + 1
            if r < 0:
                return False

            i += 1

        return False
```

最坏情况还是 target 大于所有数。时间复杂度 O(m * log n)；空间复杂度 O(1)

### 单次遍历

题解中给力一个方法。（一开始自己也往这方面想了，是不是可以类似树的遍历。想 i， j 都从 0 开始，嗯 不行。）

从矩阵左下角开始遍历，如果大于 target 则往上走一行。如果小于则往右走一列。相等则返回。


```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True

        return False
```

时间复杂度 O(m + n); 空间复杂度 O(1)
