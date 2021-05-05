# [740. 删除并获得点数](https://leetcode-cn.com/problems/delete-and-earn/) - medium

<p>给你一个整数数组 <code>nums</code> ，你可以对它进行一些操作。</p>

<p>每次操作中，选择任意一个 <code>nums[i]</code> ，删除它并获得 <code>nums[i]</code> 的点数。之后，你必须删除<strong>每个</strong>等于 <code>nums[i] - 1</code> 或 <code>nums[i] + 1</code> 的元素。</p>

<p>开始你拥有 <code>0</code> 个点数。返回你能通过这些操作获得的最大点数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,2]
<strong>输出：</strong>6
<strong>解释：</strong>
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,3,3,3,4]
<strong>输出：</strong>9
<strong>解释：</strong>
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 2 * 10<sup>4</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## Solutions

### 1. 暴力 + 缓存

先将 nums 排序。接收两个参数：当前数下标 i 和上一次选择的数字 v。如果当前数等于 v + 1，当前数不可选。否则返回选择和不选择当前数和较大的情况。

```py
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:        
        nums.sort()
        n = len(nums)

        @functools.cache
        def dfs(i: int, v: int) -> int:
            if i == n:
                return 0

            j = i
            while j < n and nums[i] == nums[j]:
                j += 1
            s1 = dfs(j, -1)
            if nums[i] == v + 1:
                return s1
                
            s2 = dfs(j, nums[i]) + nums[i] * (j - i)
            return max(s1, s2)

        return dfs(0, -1)
```

### 2. 动态规划

类似于 [198. 打家劫舍](./198-house-robber.md)

每个数有两种状态，选择 & 不选择。

- 选择 s1 分为两种情况，`nums[i] == nums[i - 1] + 1`，如果 true，则只能从前一天不选择状态转移。否则从 max(s1, s2) 状态转移。
- 不选择 s2 直接取 max(s1, s2)

时间复杂度 O(n logn), 空间复杂度 O(1)

```py
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        s1, s2 = 0, 0
        i = 0
        while i < n:
            v = nums[i]
            j = i
            while j < n and nums[j] == v:
                j += 1

            bs = s2
            s2 = max(s1, s2)
            if nums[i - 1] + 1 != v:
                bs = s2
            s1 = bs + v * (j - i)
            i = j

        return max(s1, s2)
```


### 3. 动态规划

参考题解。使用 total[v] 表示选择数字 v 增加总点数。将问题转变为一个 [0, max(nums)] 之间不可以连续选择的问题（打家劫舍问题）。

使用 `llv` 表示上上数总的收益，`lv` 表示上一个数总收益。则有：

- 当前数字选择，只能从上上数选。即 `llv + ns[i]`。当前数不选，收益为 `lv`
- 当前数最大收益为 max(llv + ns[i], lv)


时间复杂度为 O(n+m), 空间复杂度为 O(m)

```py
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxv = max(nums)
        total = [0] * (maxv + 1)
        for v in nums:
            total[v] += v
        
        def rob(ns: list) -> int:
            n = len(ns)

            llv, lv = ns[0], max(ns[0], ns[1])
            for i in range(2, n):
                llv, lv = lv, max(llv + ns[i], lv)
            
            return lv

        return rob(total)
```
