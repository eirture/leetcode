# [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) - medium

<p>在未排序的数组中找到第 <strong>k</strong> 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>[3,2,1,5,6,4] 和</code> k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6] 和</code> k = 4
<strong>输出:</strong> 4</pre>

<p><strong>说明: </strong></p>

<p>你可以假设 k 总是有效的，且 1 &le; k &le; 数组的长度。</p>


## thinking

### 1. 库函数排序

排序，取倒数 k 个元素
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
```

### 2. 快排 + 选择

使用快速排序，每次只考虑 k 所在的那一组数据。

> 快排使用随机 p 值，效率高很多。

## code

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, h = 0, len(nums) - 1
        m = len(nums)
        k = m - k
        while m != k:
            if m < k:
                l = m+1
            else:
                h = m-1
            m = self.quick_sort(nums, l, h)
        return nums[m]

    def quick_sort(self, nums: List[int], l: int, h: int) -> int:
        # 随机 p 值
        i = random.randint(l, h)
        nums[l], nums[i] = nums[i], nums[l]

        p = nums[l]

        while l < h:
            while nums[h] >= p and h > l:
                h -= 1
            nums[l] = nums[h]
 
            while nums[l] < p and l < h:
                l += 1
            nums[h] = nums[l]

        nums[l] = p
        return l
```
