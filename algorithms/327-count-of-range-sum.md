# [327. 区间和的个数](https://leetcode-cn.com/problems/count-of-range-sum/) - hard

<p>给定一个整数数组 <code>nums</code> 。区间和 <code>S(i, j)</code> 表示在 <code>nums</code> 中，位置从 <code>i</code> 到 <code>j</code> 的元素之和，包含 <code>i</code> 和 <code>j</code> (<code>i</code> ≤ <code>j</code>)。</p>

<p>请你以下标 <code>i</code> （<code>0 <= i <= nums.length</code> ）为起点，元素个数逐次递增，计算子数组内的元素和。</p>

<p>当元素和落在范围 <code>[lower, upper]</code> （包含 <code>lower</code> 和 <code>upper</code>）之内时，记录子数组当前最末元素下标 <code>j</code> ，记作 <strong>有效</strong> 区间和 <code>S(i, j)</code> 。</p>

<p>求数组中，值位于范围 <code>[lower, upper]</code> （包含 <code>lower</code> 和 <code>upper</code>）之内的 <strong>有效</strong> 区间和的个数。</p>

<p> </p>

<p><strong>注意：</strong><br />
最直观的算法复杂度是 <em>O</em>(<em>n</em><sup>2</sup>) ，请在此基础上优化你的算法。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong><em>nums</em> = <code>[-2,5,-1]</code>, <em>lower</em> = <code>-2</code>, <em>upper</em> = <code>2</code>,
<strong>输出：</strong>3 
<strong>解释：</strong>
下标 i = 0 时，子数组 [-2]、[-2,5]、[-2,5,-1]，对应元素和分别为 -2、3、2 ；其中 -2 和 2 落在范围 [lower = -2, upper = 2] 之间，因此记录有效区间和 S(0,0)，S(0,2) 。
下标 i = 1 时，子数组 [5]、[5,-1] ，元素和 5、4 ；没有满足题意的有效区间和。
下标 i = 2 时，子数组 [-1] ，元素和 -1 ；记录有效区间和 S(2,2) 。
故，共有 3 个有效区间和。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 10^4</code></li>
</ul>


## thinking

### 1. 前缀和数组 + 暴力

假设前缀和数组为 `prefix_sum`, 那么一定有 `j >= i` 且 `prefix_sum[j] - prefix_sum[i] ∈ [lower, height]`。

先构建前缀和数组，再暴力计算满足 `i, j` 对的个数，就是结果。

空间复杂度为 `O(n)` 时间复杂度为 `O(n^2)`

会超时。

### 2. 前缀和数组 + 归并排序

`TODO:2021/03/21` 这个看了题解，没有理解

## code

前缀和 + 暴力

```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        prefix_sum = [0 for _ in range(len(nums) + 1)]
        for i, v in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + v

        cnt = 0
        for i in range(len(prefix_sum)):
            j = i + 1
            while j < len(prefix_sum):
                v = prefix_sum[j] - prefix_sum[i]
                if lower <= v <= upper:
                    cnt += 1
                j += 1

        return cnt
```

前缀和 + 归并排序

```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        def merge_count(arr: List[int]) -> int:
            n = len(arr)
            if n <= 1:
                return 0
            
            n1 = [i for i in arr[:int(n/2)]]
            n2 = [i for i in arr[int(n/2):]]
            cnt = merge_count(n1) + merge_count(n2)

            l, r = 0, 0
            for v in n1:
                while l < len(n2) and n2[l] - v < lower:
                    l += 1
                while r < len(n2) and n2[r] - v <= upper:
                    r += 1
                cnt += (r - l)
            
            p1, p2 = 0, 0
            for i, _ in enumerate(arr):
                if p1 < len(n1) and (p2 == len(n2) or n1[p1] <= n2[p2]):
                    arr[i] = n1[p1]
                    p1 += 1
                else:
                    arr[i] = n2[p2]
                    p2 += 1
            
            return cnt
        
        prefix_sum = [0 for _ in range(len(nums) + 1)] 
        for i, v in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + v
        
        return merge_count(prefix_sum)
```