# [560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/) - medium

<p>给定一个整数数组和一个整数&nbsp;<strong>k，</strong>你需要找到该数组中和为&nbsp;<strong>k&nbsp;</strong>的连续的子数组的个数。</p>

<p><strong>示例 1 :</strong></p>

<pre>
<strong>输入:</strong>nums = [1,1,1], k = 2
<strong>输出:</strong> 2 , [1,1] 与 [1,1] 为两种不同的情况。
</pre>

<p><strong>说明 :</strong></p>

<ol>
	<li>数组的长度为 [1, 20,000]。</li>
	<li>数组中元素的范围是 [-1000, 1000] ，且整数&nbsp;<strong>k&nbsp;</strong>的范围是&nbsp;[-1e7, 1e7]。</li>
</ol>


## Solutions

这个问题有点类似于 [327. 区间和的个数](./327-count-of-range-sum.md)，但是其实更简单。

和为 K 的子数组，用前缀和，在遍历计算前缀和的时候，缓存前面前缀和出现的次数。假设当前遍历到 j 位，前面又 i1, i2 前缀和满足 `pre[j] - pre[i] = k`。出现次数就是 j 为右边界可以组成满足条件的子数组个数。

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}
        pre, cnt = 0, 0
        for n in nums:
            pre += n
            cnt += cache.get(pre-k, 0)
            if pre not in cache:
                cache[pre] = 0
            cache[pre] += 1
        return cnt
```
