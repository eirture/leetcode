# [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) - medium

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，请你返回其中出现频率前 <code>k</code> 高的元素。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>nums = [1,1,1,2,2,3], k = 2
<strong>输出: </strong>[1,2]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>nums = [1], k = 1
<strong>输出: </strong>[1]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>k</code> 的取值范围是 <code>[1, 数组中不相同的元素的个数]</code></li>
	<li>题目数据保证答案唯一，换句话说，数组中前 <code>k</code> 个高频元素的集合是唯一的</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你所设计算法的时间复杂度 <strong>必须</strong> 优于 <code>O(n log n)</code> ，其中 <code>n</code><em> </em>是数组大小。</p>


## Solutions

### 1. 堆排序

先用 map 记录每个数字出现的次数，然后求前 k 大次数。最近在学习堆，第一反应想到堆排序

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        
        vs = [(k, v) for k, v in m.items()]

        def sink(k: int, n: int):
            l = k * 2  + 1
            r = l + 1

            if l > n:
                return
            
            idx = l
            if r <= n and vs[r][1] > vs[l][1]:
                idx = r
            
            if vs[idx][1] <= vs[k][1]:
                return
            
            vs[idx], vs[k] = vs[k], vs[idx]
            sink(idx, n)
        
        c = len(vs) // 2 - 1
        for i in range(c, -1, -1):
            sink(i, len(vs) - 1)

        results = []
        n = len(vs) - 1
        for i in range(k):
            vs[n], vs[0] = vs[0], vs[n]
            results.append(vs[n][0])
            n -= 1
            sink(0, n)
        
        return results
```

### 2. 快排 + 选择

类似于 [215. 数组中的第K个最大元素](./215-kth-largest-element-in-an-array.md)

快速排序，如果快排分割点等于 `len(vs) - k` 则右侧就是 top-k；如果小于则继续排右侧，否则继续排左侧。

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        
        vs = [(k, v) for k, v in m.items()]

        def patition(l: int, r: int) -> int:
            p = vs[l]

            while l < r:
                while r > l and vs[r][1] > p[1]:
                    r -= 1
                vs[l] = vs[r]

                while l < r and vs[l][1] <= p[1]:
                    l += 1
                vs[r] = vs[l]
            vs[l] = p
            return l
        
        l, r = 0, len(vs) - 1
        n = len(vs)
        idx = len(vs) - k
        while n != idx:
            if n < idx:
                l = n + 1
            else:
                r = n - 1
            n = patition(l, r)

        return [v[0] for v in vs[n:]]
```
