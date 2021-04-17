# [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/) - medium

<p>给定一个包含 <code>n + 1</code> 个整数的数组 <code>nums</code> ，其数字都在 <code>1</code> 到 <code>n</code><em> </em>之间（包括 <code>1</code> 和 <code>n</code>），可知至少存在一个重复的整数。</p>

<p>假设 <code>nums</code> 只有 <strong>一个重复的整数</strong> ，找出 <strong>这个重复的数</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 3 * 10<sup>4</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 <= nums[i] <= n</code></li>
	<li><code>nums</code> 中 <strong>只有一个整数</strong> 出现 <strong>两次或多次</strong> ，其余整数均只出现 <strong>一次</strong></li>
</ul>

<p> </p>

<p><b>进阶：</b></p>

<ul>
	<li>如何证明 <code>nums</code> 中至少存在一个重复的数字?</li>
	<li>你可以在不修改数组 <code>nums</code> 的情况下解决这个问题吗？</li>
	<li>你可以只用常量级 <code>O(1)</code> 的额外空间解决这个问题吗？</li>
	<li>你可以设计一个时间复杂度小于 <code>O(n<sup>2</sup>)</code> 的解决方案吗？</li>
</ul>


## Solutions

### 1. hash 缓存

用一个 hash 表缓存遍历过的数据

时间复杂度 O(n); 空间复杂度 O(n)

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if m.get(n, False):
                return n
            m[n] = True
```

### 2. 排序后遍历

先排序，然后遍历比较 i 和 i + 1 值

时间复杂度取排序: O(n log n)

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        
```

### 3. 还原位置

因为 nums 中的数据对应他们的 index，遍历并将每个数还原到对应的 index。还原过程中如果对应 index 已经存在这个数，表示这个数重复

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):

            if nums[i] == i + 1:
                continue
            
            v = nums[i]
            j = nums[i] - 1
            while j != i:
                if nums[j] == v:
                    return v

                nums[j], v = v, nums[j]
                j = v - 1
            
            nums[i] = v
```


### 4. 快慢指针

把这个数组当一个链表，重复元素就是环点。通过快慢指针，当快慢指针相遇时，相遇点到环点的距离，等于表头到环点的距离（证明见 [100168. 环路检测](./100168-linked-list-cycle-lcci.md#thinking)）。

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l, f = 0, 0

        while True:
            l = nums[l]
            f = nums[nums[f]]
            if l == f:
                break

        l = 0
        while l != f:
            l = nums[l]
            f = nums[f]

        return l
```
