# [633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/) - medium

<p>给定一个非负整数&nbsp;<code>c</code>&nbsp;，你要判断是否存在两个整数 <code>a</code> 和 <code>b</code>，使得&nbsp;<code>a<sup>2</sup> + b<sup>2</sup> = c</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>c = 5
<strong>输出：</strong>true
<strong>解释：</strong>1 * 1 + 2 * 2 = 5
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>c = 3
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>c = 4
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>c = 2
<strong>输出：</strong>true
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>c = 1
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solutions

### 1. 二分搜索

把所有可能的值列举出来，固定一个值 v，然后二分搜索剩下部分，是否存在等于 `ns[x] = c - v`

时间复杂度为 O(n*log n); 空间复杂度为 O(c ** 0.5)

```py
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ns = [i ** 2 for i in range(int(c ** 0.5) + 1)]
        
        n = len(ns)
        x = int((c // 2) ** 0.5) + 1
        for l, v in enumerate(ns):
            r = n - 1
            y = c - v
            while l <= r:
                m = (l + r) // 2
                if ns[m] == y:
                    return True
                if ns[m] < y:
                    l = m + 1
                else:
                    r = m - 1
        
        return False
```

### 2. 遍历

遍历 [0, c ** 0.5] 判断 c - i 是否为有平方根

时间复杂度 O(c ** 0.5)；空间复杂度 O(1)

```py
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 0
        while i ** 2 <= c:
            y = (c - i ** 2) ** 0.5
            if y == int(y):
                return True
            i += 1

        return False
```

### 3. 双指针

设两个指针，l = 0, r = int(c ** 0.5)，求出 `v = l ** 2 + r ** 2`

- v == c 返回 True
- v < c 则 l += 1
- v > c 则 r -= 1

当 l > r 时结束

```py
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        l = 0
        r = int(c ** 0.5)

        while l <= r:
            v = l ** 2 + r ** 2
            if v == c:
                return True
            if v < c:
                l += 1
            else:
                r -= 1
        
        return False
```
