# [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/) - easy

<p>给你一个 32 位的有符号整数 <code>x</code> ，返回将 <code>x</code> 中的数字部分反转后的结果。</p>

<p>如果反转后整数超过 32 位的有符号整数的范围 <code>[−2<sup>31</sup>,  2<sup>31 </sup>− 1]</code> ，就返回 0。</p>
<strong>假设环境不允许存储 64 位整数（有符号或无符号）。</strong>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 123
<strong>输出：</strong>321
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = -123
<strong>输出：</strong>-321
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 120
<strong>输出：</strong>21
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>x = 0
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code></li>
</ul>


## Solutions

### 1. 字符串反转

python3 中没有 long 类型，所以其 int 可以表示 64 bit 数字，做一下边界判断

```py3
class Solution:
    def reverse(self, x: int) -> int:
        vs = str(x)
        ans = ''.join(list(reversed(vs)))
        if x < 0:
            v = -int(ans[:-1])
            return 0 if v < (-1 << 31) else v
        
        v = int(ans)
        return 0 if v > (1 << 31) - 1 else v
```

### 2. 数字处理

对 10 取余 i, 结果值 `ans * 10 + i`

```py3
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        f = 1
        if x < 0:
            f = -1
            x *= -1

        while x != 0:
            i = x % 10
            ans *= 10
            ans += i
            x //= 10
        
        ans *= f
        if -1 << 31 <= ans <= (1 << 31) - 1:
            return ans
        return 0
```
