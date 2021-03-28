# [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/) - medium

<p>给定一个字符串&nbsp;<strong>s&nbsp;</strong>和一个非空字符串&nbsp;<strong>p</strong>，找到&nbsp;<strong>s&nbsp;</strong>中所有是&nbsp;<strong>p&nbsp;</strong>的字母异位词的子串，返回这些子串的起始索引。</p>

<p>字符串只包含小写英文字母，并且字符串&nbsp;<strong>s&nbsp;</strong>和 <strong>p&nbsp;</strong>的长度都不超过 20100。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>字母异位词指字母相同，但排列不同的字符串。</li>
	<li>不考虑答案输出的顺序。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong>
s: &quot;cbaebabacd&quot; p: &quot;abc&quot;

<strong>输出:</strong>
[0, 6]

<strong>解释:</strong>
起始索引等于 0 的子串是 &quot;cba&quot;, 它是 &quot;abc&quot; 的字母异位词。
起始索引等于 6 的子串是 &quot;bac&quot;, 它是 &quot;abc&quot; 的字母异位词。
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入:</strong>
s: &quot;abab&quot; p: &quot;ab&quot;

<strong>输出:</strong>
[0, 1, 2]

<strong>解释:</strong>
起始索引等于 0 的子串是 &quot;ab&quot;, 它是 &quot;ab&quot; 的字母异位词。
起始索引等于 1 的子串是 &quot;ba&quot;, 它是 &quot;ab&quot; 的字母异位词。
起始索引等于 2 的子串是 &quot;ab&quot;, 它是 &quot;ab&quot; 的字母异位词。
</pre>


## Solutions

### 1. 使用 Hash

用 map m 存储 p 中元素个数。再用快慢指针（滑动窗口）对 m 做操作。当某个字母个数为 0 时。将它从 m 删除。如果某一次滑动 `len(m) == 0`。此时 l 就是满足条件的值之一。一直滑动到 s 末尾。

```python
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        m = defaultdict(lambda: 0)
        for i in p:
            m[i] += 1
        
        def add(v):
            m[v] += 1
            if m[v] == 0:
                del m[v]
        
        def rm(v):
            m[v] -= 1
            if m[v] == 0:
                del m[v]
        
        results = []
        l, r = 0, 0
        while r < len(p):
            rm(s[r])
            r += 1

        while r < len(s):
            if len(m) == 0:
                results.append(l)
            rm(s[r])
            r += 1
            add(s[l])
            l += 1

        if len(m) == 0:
            results.append(l)

        return results
```
