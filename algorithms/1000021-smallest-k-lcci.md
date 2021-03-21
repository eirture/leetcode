# [1000021. 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci/) - medium

<p>设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong> arr = [1,3,5,7,2,4,6,8], k = 4
<strong>输出：</strong> [1,2,3,4]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(arr) &lt;= 100000</code></li>
	<li><code>0 &lt;= k &lt;= min(100000, len(arr))</code></li>
</ul>


## thinking

### 1. 快排加选择

refer to [215. 数组中的第K个最大元素](./215-kth-largest-element-in-an-array.md)

## code

```python
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        
        if not arr:
            return arr

        l, h = 0, len(arr) - 1
        m = self.part(arr, l, h)
        
        while m != k:
            if m < k:
                l = m + 1
            else:
                h = m - 1
            m = self.part(arr, l, h)
        return arr[:m]

    def quick_sort(self, arr: List[int], l: int, r: int):
        if l >= r:
            return

        m = self.part(arr, l, r)
        self.quick_sort(arr, l, m - 1)
        self.quick_sort(arr, m + 1, r)

    def part(self, arr: List[int], l: int, r: int) -> int:
        p = arr[l]

        while l < r:
            while arr[r] >= p and l < r:
                r -= 1
            arr[l] = arr[r]

            while arr[l] < p and l < r:
                l += 1
            arr[r] = arr[l]
        
        arr[l] = p
        return l
```

