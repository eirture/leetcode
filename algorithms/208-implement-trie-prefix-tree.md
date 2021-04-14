# [208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) - medium

<p><strong><a href="https://baike.baidu.com/item/字典树/9825209?fr=aladdin" target="_blank">Trie</a></strong>（发音类似 "try"）或者说 <strong>前缀树</strong> 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。</p>

<p>请你实现 Trie 类：</p>

<ul>
	<li><code>Trie()</code> 初始化前缀树对象。</li>
	<li><code>void insert(String word)</code> 向前缀树中插入字符串 <code>word</code> 。</li>
	<li><code>boolean search(String word)</code> 如果字符串 <code>word</code> 在前缀树中，返回 <code>true</code>（即，在检索之前已经插入）；否则，返回 <code>false</code> 。</li>
	<li><code>boolean startsWith(String prefix)</code> 如果之前已经插入的字符串 <code>word</code> 的前缀之一为 <code>prefix</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>输出</strong>
[null, null, true, false, true, null, true]

<strong>解释</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= word.length, prefix.length <= 2000</code></li>
	<li><code>word</code> 和 <code>prefix</code> 仅由小写英文字母组成</li>
	<li><code>insert</code>、<code>search</code> 和 <code>startsWith</code> 调用次数 <strong>总计</strong> 不超过 <code>3 * 10<sup>4</sup></code> 次</li>
</ul>


## Solutions


### 1. map 树

```py
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        m = self.m
        n = Node()
        for s in word:
            n = m.get(s, Node())
            m[s] = n
            m = n.m
        n.f = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        m = self.m
        n = Node()
        for s in word:
            if s not in m:
                return False
            n = m[s]
            m = n.m
        return n.f

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        m = self.m
        for s in prefix:
            if s not in m:
                return False
            m = m[s].m
        return True

class Node:
    def __init__(self, f=False):
        self.f = f
        self.m = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

题目中说明 word 和 prefix 只包含小写字母，可以将 map 替换为 list 节省存储空间。

```py
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isend = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tn = self
        for s in word:
            idx = ord(s) - ord('a')
            if tn.children[idx] is None:
                tn.children[idx] = Trie()
            tn = tn.children[idx]
        tn.isend = True

    def _search(self, word: str) -> 'Trie':
        tn = self
        for s in word:
            idx = ord(s) - ord('a')
            if tn.children[idx] is None:
                return None
            tn = tn.children[idx]
        return tn

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tn = self._search(word)
        return bool(tn and tn.isend)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```