# [190. 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/) - easy

<p>颠倒给定的 32 位无符号整数的二进制位。</p>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。</li>
	<li>在 Java 中，编译器使用<a href="https://baike.baidu.com/item/二进制补码/5295284" target="_blank">二进制补码</a>记法来表示有符号整数。因此，在上面的 <strong>示例 2</strong> 中，输入表示有符号整数 <code>-3</code>，输出表示有符号整数 <code>-1073741825</code>。</li>
</ul>

<p> </p>

<p><strong>进阶</strong>:<br />
如果多次调用这个函数，你将如何优化你的算法？</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> 00000010100101000001111010011100
<strong>输出:</strong> 00111001011110000010100101000000
<strong>解释: </strong>输入的二进制串 <strong>00000010100101000001111010011100 </strong>表示无符号整数<strong> 43261596</strong><strong>，
</strong>     因此返回 964176192，其二进制表示形式为 <strong>00111001011110000010100101000000</strong>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>11111111111111111111111111111101
<strong>输出：</strong>10111111111111111111111111111111
<strong>解释：</strong>输入的二进制串 <strong>11111111111111111111111111111101</strong> 表示无符号整数 4294967293，
     因此返回 3221225471 其二进制表示形式为 <strong>10111111111111111111111111111111 。</strong></pre>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 00000010100101000001111010011100
<strong>输出：</strong>964176192 (00111001011110000010100101000000)
<strong>解释：</strong>输入的二进制串 <strong>00000010100101000001111010011100 </strong>表示无符号整数<strong> 43261596</strong><strong>，
    </strong> 因此返回 964176192，其二进制表示形式为 <strong>00111001011110000010100101000000</strong>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 11111111111111111111111111111101
<strong>输出：</strong>3221225471 (10111111111111111111111111111111)
<strong>解释：</strong>输入的二进制串 <strong>11111111111111111111111111111101</strong> 表示无符号整数 4294967293，
     因此返回 3221225471 其二进制表示形式为 <strong>10111111111111111111111111111111 。</strong></pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>输入是一个长度为 <code>32</code> 的二进制字符串</li>
</ul>


## Solutions

### 1. 位运算

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        v = 0
        for i in range(32):
            v <<= 1
            v |= n & 1
            n >>= 1
        return v
```

题解中有个[使用分治的巧妙解法](https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode-solu-yhxz/#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E4%BD%8D%E8%BF%90%E7%AE%97%E5%88%86%E6%B2%BB)。
