# [179. 最大数](https://leetcode-cn.com/problems/largest-number/) - medium

<p>给定一组非负整数 <code>nums</code>，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。</p>

<p><strong>注意：</strong>输出结果可能非常大，所以你需要返回一个字符串而不是整数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入<code>：</code></strong><code>nums = [10,2]</code>
<strong>输出：</strong><code>"210"</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入<code>：</code></strong><code>nums = [3,30,34,5,9]</code>
<strong>输出：</strong><code>"9534330"</code>
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入<code>：</code></strong>nums = [1]
<strong>输出：</strong>"1"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入<code>：</code></strong>nums = [10]
<strong>输出：</strong>"10"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 100</code></li>
	<li><code>0 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>


## Solutions

### 1. 排序

看了题解，证明两个数 x, y 拼接起来时，直接比较 `xy` 和 `yx` 谁更大就取对应的排列次序。

```py
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp(x, y) -> int:
            sx, sy = 10, 10
            while sx <= x:
                sx *= 10
            
            while sy <= y:
                sy *= 10
            
            return (sy * x + y) - (sx * y + x)

        nums.sort(key=functools.cmp_to_key(cmp), reverse=True)
        
        if nums[0] == 0:
            return "0"

        return ''.join(str(i) for i in nums)
```
