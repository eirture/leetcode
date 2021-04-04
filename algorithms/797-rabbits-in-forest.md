# [797. 森林中的兔子](https://leetcode-cn.com/problems/rabbits-in-forest/) - medium

<p>森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在&nbsp;<code>answers</code>&nbsp;数组里。</p>

<p>返回森林中兔子的最少数量。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> answers = [1, 1, 2]
<strong>输出:</strong> 5
<strong>解释:</strong>
两只回答了 &quot;1&quot; 的兔子可能有相同的颜色，设为红色。
之后回答了 &quot;2&quot; 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 &quot;2&quot; 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

<strong>输入:</strong> answers = [10, 10, 10]
<strong>输出:</strong> 11

<strong>输入:</strong> answers = []
<strong>输出:</strong> 0
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>answers</code>&nbsp;的长度最大为<code>1000</code>。</li>
	<li><code>answers[i]</code>&nbsp;是在&nbsp;<code>[0, 999]</code>&nbsp;范围内的整数。</li>
</ol>


## Solutions

按照个数统计，然后求每个个数对应最小数量。假设 有 5 只兔子说有其他 3 只跟自己同样颜色。最小可能就是 4 个是同一个颜色，1 个另一种颜色。总共两种颜色。

时间复杂度 O(n)，空间复杂度 O(n)

```py
from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = defaultdict(lambda: 0)

        for i in answers:
            c[i] += 1
        
        ans = 0
        for k, v in c.items():
            n = k + 1
            ans += n * ((v - 1) // n + 1)

        return ans
```
