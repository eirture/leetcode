# [2654. 统计范围内的元音字符串数](https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/) - easy

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 和两个整数：<code>left</code> 和 <code>right</code> 。</p>

<p>如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 <strong>元音字符串</strong> ，其中元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code>、<code>'u'</code> 。</p>

<p>返回<em> </em><code>words[i]</code> 是元音字符串的数目，其中<em> </em><code>i</code> 在闭区间 <code>[left, right]</code> 内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["are","amy","u"], left = 0, right = 2
<strong>输出：</strong>2
<strong>解释：</strong>
- "are" 是一个元音字符串，因为它以 'a' 开头并以 'e' 结尾。
- "amy" 不是元音字符串，因为它没有以元音字母结尾。
- "u" 是一个元音字符串，因为它以 'u' 开头并以 'u' 结尾。
在上述范围中的元音字符串数目为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
<strong>输出：</strong>3
<strong>解释：</strong>
- "aeo" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
- "mu" 不是元音字符串，因为它没有以元音字母开头。
- "ooo" 是一个元音字符串，因为它以 'o' 开头并以 'o' 结尾。
- "artro" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
在上述范围中的元音字符串数目为 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>0 &lt;= left &lt;= right &lt; words.length</code></li>
</ul>


## Solutions

### 1. 遍历

最简单的方法就是便利一遍，查看每个单词第一个字母和最后一个字母是否为元音。判断的方法很多，比较常用的是用 map 保存所有元音字母。我这里用了一个 swtich。

时间复杂度为 O(n)；空间复杂度为 O(1)

```go
func vowelStrings(words []string, left int, right int) int {
    var count int
    for _, w := range words[left:right+1] {
        if isVowel(w[0]) && isVowel(w[len(w)-1]) {
            count++
        }
    }
    return count
}

func isVowel(v byte) bool {
    switch v {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    default :
        return false
    }
}
```
