# [227. 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/) - medium

<p>给你一个字符串表达式 <code>s</code> ，请你实现一个基本计算器来计算并返回它的值。</p>

<p>整数除法仅保留整数部分。</p>

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "3+2*2"
<strong>输出：</strong>7
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = " 3/2 "
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = " 3+5 / 2 "
<strong>输出：</strong>5
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 由整数和算符 <code>('+', '-', '*', '/')</code> 组成，中间由一些空格隔开</li>
	<li><code>s</code> 表示一个 <strong>有效表达式</strong></li>
	<li>表达式中的所有整数都是非负整数，且在范围 <code>[0, 2<sup>31</sup> - 1]</code> 内</li>
	<li>题目数据保证答案是一个 <strong>32-bit 整数</strong></li>
</ul>
</div>
</div>


## Solutions

### 1. 先分解成数字和运算符数组，再用栈计算

与 [1048. 笨阶乘](./1048-clumsy-factorial.md) 类似.

```py
class Solution:
    def calculate(self, s: str) -> int:
        
        vs = [0]
        for v in s:
            if v == ' ':
                continue

            if v in ['+', '-', '*', '/']:
                vs.append(v)
                vs.append(0)
            else:
                vs[-1] *= 10
                vs[-1] += int(v)

        st = [vs[0]]
        i = 1
        while i < len(vs):
            n = vs[i]
            if n == '+':
                st.append(vs[i + 1])
            elif n == '-':
                st.append(-vs[i + 1])
            elif n == '*':
                st[-1] *= vs[i + 1]
            elif n == '/':
                st[-1] = int(st[-1] / vs[i + 1])
            i += 2

        return sum(st)
```

参考题解，一遍遍历计算结果

```py
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        vs = []

        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i] not in '+-*/':
                num *= 10
                num += int(s[i])
            # 最后一次 i == n 时，也要走这个分支
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    vs.append(num)
                elif preSign == '-':
                    vs.append(-num)
                elif preSign == '*':
                    vs[-1] *= num
                else:
                    vs[-1] = int(vs[-1] / num)
                preSign = s[i]
                num = 0

        return sum(vs)

```