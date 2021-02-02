# [29. 两数相除](https://leetcode-cn.com/problems/divide-two-integers) - medium

<p>给定两个整数，被除数&nbsp;<code>dividend</code>&nbsp;和除数&nbsp;<code>divisor</code>。将两数相除，要求不使用乘法、除法和 mod 运算符。</p>

<p>返回被除数&nbsp;<code>dividend</code>&nbsp;除以除数&nbsp;<code>divisor</code>&nbsp;得到的商。</p>

<p>整数除法的结果应当截去（<code>truncate</code>）其小数部分，例如：<code>truncate(8.345) = 8</code> 以及 <code>truncate(-2.7335) = -2</code></p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> dividend = 10, divisor = 3
<strong>输出:</strong> 3
<strong>解释: </strong>10/3 = truncate(3.33333..) = truncate(3) = 3</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> dividend = 7, divisor = -3
<strong>输出:</strong> -2
<strong>解释:</strong> 7/-3 = truncate(-2.33333..) = -2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>被除数和除数均为 32 位有符号整数。</li>
	<li>除数不为&nbsp;0。</li>
	<li>假设我们的环境只能存储 32 位有符号整数，其数值范围是 [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。本题中，如果除法结果溢出，则返回 2<sup>31&nbsp;</sup>&minus; 1。</li>
</ul>


## thinking

## code
```python
def divide(dividend, divisor):
    is_negative = (dividend < 0) != (divisor < 0)
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = -divisor

    i = 0
    step = divisor
    step_count = 1
    begin_reduce = False

    step_list = []
    index = 0
    while dividend >= divisor:

        # print(dividend, step)
        while dividend < step and index >= 0:
            step, step_count = step_list[index]
            index -= 1

        if index < 0 and dividend < step:
            break

        dividend -= step
        i += step_count

        if not begin_reduce:
            step_list.append((step, step_count))
            step += step
            step_count += step_count
            index = len(step_list) - 1

    if is_negative:
        return max(-i, -1 << 31)
    return min(i, (1 << 31) - 1)
```
