# [91. 解码方法](https://leetcode-cn.com/problems/decode-ways/) - medium

<p>一条包含字母 <code>A-Z</code> 的消息通过以下映射进行了 <strong>编码</strong> ：</p>

<pre>
'A' -> 1
'B' -> 2
...
'Z' -> 26
</pre>

<p>要 <strong>解码</strong> 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，<code>"11106"</code> 可以映射为：</p>

<ul>
	<li><code>"AAJF"</code> ，将消息分组为 <code>(1 1 10 6)</code></li>
	<li><code>"KJF"</code> ，将消息分组为 <code>(11 10 6)</code></li>
</ul>

<p>注意，消息不能分组为  <code>(1 11 06)</code> ，因为 <code>"06"</code> 不能映射为 <code>"F"</code> ，这是由于 <code>"6"</code> 和 <code>"06"</code> 在映射中并不等价。</p>

<p>给你一个只含数字的 <strong>非空 </strong>字符串 <code>s</code> ，请计算并返回 <strong>解码</strong> 方法的 <strong>总数</strong> 。</p>

<p>题目数据保证答案肯定是一个 <strong>32 位</strong> 的整数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "12"
<strong>输出：</strong>2
<strong>解释：</strong>它可以解码为 "AB"（1 2）或者 "L"（12）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "226"
<strong>输出：</strong>3
<strong>解释：</strong>它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0"
<strong>输出：</strong>0
<strong>解释：</strong>没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "06"
<strong>输出：</strong>0
<strong>解释：</strong>"06" 不能映射到 "F" ，因为字符串含有前导 0（<code>"6"</code> 和 <code>"06"</code> 在映射中并不等价）。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code> 只包含数字，并且可能包含前导零。</li>
</ul>


## Solutions

### 1. 动态规划

（终于可以自己做出动态规划了）

用 dp[i] 表示第 i 个数最大可能。则有：

1. 如果满足 `s[i - 1] == 1` s[i] 可以是任意值，s[i-1:i+1] 可以组成有效编码，数量增加 dp[i - 2] * 1
2. 如果满足 `s[i - 2] == 2` 则 s[i] 只能取 `[0, 6]` 区间，可以组成有效编码，数量增加 dp[i - 2] * 1
3. 如果满足 `s[i] != 0` 则 s[i] 自己可以组成有效编码，数量增加 dp[i - 1] * 1

```py
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        dp = [1] * n
        for i in range(1, n):
            v = 0
            ln = int(s[i - 1])
            nv = int(s[i])
            if ln == 1 or (ln == 2 and nv <= 6):
                v += dp[i - 2]

            if nv != 0:
                v += dp[i - 1]
            
            dp[i] = v
        
        return dp[-1]
```

时间复杂度 O(n); 空间复杂度 O(n)

dp[i] 只与 dp[i - 1] 和 dp[i - 2] 有关，可以优化一下：

```py
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        llc, lc = 1, 1
        for i in range(1, n):
            v = 0
            ln = int(s[i - 1])
            nv = int(s[i])

            if ln == 1 or (ln == 2 and nv <= 6):
                v += llc

            if nv != 0:
                v += lc
            
            llc, lc = lc, v
        
        return lc
```

时间复杂度 O(n)；空间复杂度 O(1)
