# [220. 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii/) - medium

<p>给你一个整数数组 <code>nums</code> 和两个整数 <code>k</code> 和 <code>t</code> 。请你判断是否存在 <b>两个不同下标</b> <code>i</code> 和 <code>j</code>，使得 <code>abs(nums[i] - nums[j]) <= t</code> ，同时又满足 <code>abs(i - j) <= k</code><em> </em>。</p>

<p>如果存在则返回 <code>true</code>，不存在返回 <code>false</code>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], k<em> </em>= 3, t = 0
<strong>输出：</strong>true</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,1], k<em> </em>=<em> </em>1, t = 2
<strong>输出：</strong>true</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,9,1,5,9], k = 2, t = 3
<strong>输出：</strong>false</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 2 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code></li>
	<li><code>0 <= k <= 10<sup>4</sup></code></li>
	<li><code>0 <= t <= 2<sup>31</sup> - 1</code></li>
</ul>


## Solutions

### 1. 桶排序

迭代遍历 nums，将元素按照 t 划分，取 `id = n // (t + 1)` 当 `n < 0` 时 `id = int(n + 1) / (t + 1) - 1`。

假设每个元素的值和下表一致（i == n）

![](https://s.eirture.cn/pics/IMG_505D958C0CC1-1.jpeg)


因为数据不是有序的，可能 `id + 1` 出现在 `id` 前面。所以在做判断时，需要查看 `id - 1` 和 `id + 1`。

为什么桶里只有一个元素？因为如果有一个数的 id 对应的桶已经存在，说明我们已经找到结果了，就 return 了。不存在桶里有两元素情况。

```py
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        bn = t + 1
        def getid(x: int) -> int:
            return x // bn if x >= 0 else int((x + 1) / bn - 1)
        
        bs = {}
        for i, n in enumerate(nums):
            nid = getid(n)

            if nid in bs:
                return True
            
            if nid + 1 in bs and abs(bs[nid + 1] - n) <= t:
                return True
            
            if nid - 1 in bs and abs(bs[nid - 1] - n) <= t:
                return True
            
            bs[nid] = n
            if i >= k:
                bs.pop(getid(nums[i - k]), None)
            
        return False
```
