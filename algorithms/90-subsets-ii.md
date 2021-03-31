# [90. 子集 II](https://leetcode-cn.com/problems/subsets-ii/) - medium

<p>给你一个整数数组 <code>nums</code> ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。返回的解集中，子集可以按 <strong>任意顺序</strong> 排列。</p>

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2]
<strong>输出：</strong>[[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10</code></li>
	<li><code>-10 <= nums[i] <= 10</code></li>
</ul>
</div>
</div>


## Solutions

### 1. 迭代

这是 [78. 子集](78-subsets.md) 升级版本，复杂在于有重复数据。对数组先做一次排序。然后同样使用 2 进制枚举，当 `nums[i] == [nums][i-1]` 且 i-1 不选取的时候，结果一定是和只选 i-1 一样的。所以这种情况直接跳过。

```py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
  
        results = []
        n = len(nums)
        for mask in range(1 << n):
            vs = []
            skip = False
            for i in range(n):
                if mask >> i & 1:
                    if i > 0 and mask >> (i - 1) & 1 == 0 and nums[i] == nums[i - 1]:
                        skip = True
                        break
                    vs.append(nums[i])
            if not skip:
                results.append(vs)
        return results
```
