# [27. 移除元素](https://leetcode-cn.com/problems/remove-element/) - easy

<p>给你一个数组 <code>nums</code><em> </em>和一个值 <code>val</code>，你需要 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong> 移除所有数值等于 <code>val</code><em> </em>的元素，并返回移除后数组的新长度。</p>

<p>不要使用额外的数组空间，你必须仅使用 <code>O(1)</code> 额外空间并 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组</strong>。</p>

<p>元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。</p>

<p> </p>

<p><strong>说明:</strong></p>

<p>为什么返回数值是整数，但输出的答案是数组呢?</p>

<p>请注意，输入数组是以<strong>「引用」</strong>方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。</p>

<p>你可以想象内部操作如下:</p>

<pre>
// <strong>nums</strong> 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中<strong> 该长度范围内</strong> 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
</pre>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,2,3], val = 3
<strong>输出：</strong>2, nums = [2,2]
<strong>解释：</strong>函数应该返回新的长度 <strong>2</strong>, 并且 nums<em> </em>中的前两个元素均为 <strong>2</strong>。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,2,2,3,0,4,2], val = 2
<strong>输出：</strong>5, nums = [0,1,4,0,3]
<strong>解释：</strong>函数应该返回新的长度 <strong><code>5</code></strong>, 并且 nums 中的前五个元素为 <strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>3</code></strong>, <strong><code>0</code></strong>, <strong>4</strong>。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 50</code></li>
	<li><code>0 <= val <= 100</code></li>
</ul>


## Solutions

### 1. 双指针

快排思想，左边指针找到等于 val，右边指针找到不等于 val；交换。当最终两指针相遇，可能是走到结尾了，这时 nums[l] == val 不一定成立。
所以最终要做一次检查。

```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n < 1:
            return n
            
        l, r = 0, n - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1

            while l < r and nums[r] == val:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]

        return l + 1 if nums[l] != val else l
```

题解中同样使用 l, r 双指针左右往中间走。实现更简单一些：

```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        l, r = 0, n
        while l < r:
            if nums[l] == val:
                nums[l] = nums[r - 1]
                r -= 1
            else:
                l += 1

        return l
```
