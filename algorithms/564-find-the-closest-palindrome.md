# [564. 寻找最近的回文数](https://leetcode-cn.com/problems/find-the-closest-palindrome) - hard

<p>给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。</p>

<p>&ldquo;最近的&rdquo;定义为两个整数<strong>差的绝对值</strong>最小。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;123&quot;
<strong>输出:</strong> &quot;121&quot;
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><strong>n </strong>是由字符串表示的正整数，其长度不超过18。</li>
	<li>如果有多个结果，返回最小的那个。</li>
</ol>


## thinking

## code

```python

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        lg, ni = len(n), int(n)

        if ni % (10 ** (lg - 1)) == 0:
            return str(ni - 1)

        if n == '9' * lg:
            return str(ni + 2)

        a = [i for i in n]
        left, right = 0, lg - 1
        flag = True
        while left <= right:
            if flag:
                flag = a[left] == n[right]
            a[right] = n[left]
            left += 1
            right -= 1

        if flag and lg > 0:
            left -= 1
            right += 1
            v = int(a[left]) - 1
            if v == 0 and lg == 2:
                return "9"

            if v < 0:
                if left == right:
                    a[left] = str(v + 2)
                while v < 0 and left >= 1:
                    a[left] = a[right] = '9'
                    left -= 1
                    right += 1
                    v = int(a[left]) - 1

            a[left] = a[right] = str(v)
        return ''.join(a)

```