# [338. 比特位计数](https://leetcode-cn.com/problems/counting-bits/) - medium

<p>给定一个非负整数&nbsp;<strong>num</strong>。对于&nbsp;<strong>0 &le; i &le; num </strong>范围中的每个数字&nbsp;<strong>i&nbsp;</strong>，计算其二进制数中的 1 的数目并将它们作为数组返回。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>2
<strong>输出: </strong>[0,1,1]</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong>5
<strong>输出: </strong><code>[0,1,1,2,1,2]</code></pre>

<p><strong>进阶:</strong></p>

<ul>
	<li>给出时间复杂度为<strong>O(n*sizeof(integer))</strong>的解答非常容易。但你可以在线性时间<strong>O(n)</strong>内用一趟扫描做到吗？</li>
	<li>要求算法的空间复杂度为<strong>O(n)</strong>。</li>
	<li>你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的&nbsp;<strong>__builtin_popcount</strong>）来执行此操作。</li>
</ul>


## Solutions

### 1. 动态规划 + 最高有效位

当 `i & (i - 1) == 0` 时，说明 i 是 2 的 n 次方。此时 `bits[i] = 1`。记此时 i 为最高有效位 hb，有 `bits[i] = bits[i - hb] + 1`（i - hb 就是去掉最高位的 1）。

```py
class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        hb = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                hb = i
                bits[i] = 1
            else:
                bits[i] = bits[i - hb] + 1
            
        return bits
```

时间复杂度 O(n)；空间复杂度 O(1)

### 2. 动态规划 + 最低有效位

将 `i` 右移一位，则有 `bits[i] = bits[i >> 1] + 1` 当 i 是奇数; `bits[i] = bits[i >> 1]` 当 i 是偶数。i >> 1 = i/2, 一定有 `i/2 < i` 所以可以利用前面的计算结果。

```py
class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        for i in range(1, num + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
```

时间负责度：O(n)；空间复杂度：O(1)

### 3. 动态规划 + 最低设置位

将 i 最后一位 1 变成 0 的运算为 `i & (i - 1)`，当 i > 0 时，有`i & (i - 1) < i`。那就有 `bits[i] = bits[i & (i - 1)] + 1`

```py
class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        for i in range(1, num + 1):
            bits[i] = bits[i & (i - 1)] + 1
        return bits
```
