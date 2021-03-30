# [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/) - medium

<p>编写一个高效的算法来判断 <code>m x n</code> 矩阵中，是否存在一个目标值。该矩阵具有如下特性：</p>

<ul>
	<li>每行中的整数从左到右按升序排列。</li>
	<li>每行的第一个整数大于前一行的最后一个整数。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>-10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup></code></li>
</ul>


## Solutions

### 1. 二分查找

先定位行，再定位值。

时间复杂度 O(log m + log n) = O(log m*n)；空间复杂度 O(1)

```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False

        def findrow(l, r) -> int:
            if l + 1 == r:
                return l
            m = (l + r) // 2
            if matrix[m][0] <= target:
                return findrow(m, r)
            return findrow(l, m)

        r = findrow(0, len(matrix))

        def find(nums: List[int], l, r) -> bool:
            if l >= r:
                return nums[l] == target
            m = (l + r) // 2
            if nums[m] < target:
                return find(nums, m+1, r)
            return find(nums, l, m)

        return find(matrix[r], 0, len(matrix[r]) - 1)

```

题解中有个思路，将每行连起来看作是一个升序数组，一次二分查找即可。
