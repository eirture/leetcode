# [1000051. 稀疏相似度](https://leetcode-cn.com/problems/sparse-similarity-lcci/) - hard

<p>两个(具有不同单词的)文档的交集(intersection)中元素的个数除以并集(union)中元素的个数，就是这两个文档的相似度。例如，{1, 5, 3} 和 {1, 7, 2, 3} 的相似度是 0.4，其中，交集的元素有 2 个，并集的元素有 5 个。给定一系列的长篇文档，每个文档元素各不相同，并与一个 ID 相关联。它们的相似度非常&ldquo;稀疏&rdquo;，也就是说任选 2 个文档，相似度都很接近 0。请设计一个算法返回每对文档的 ID 及其相似度。只需输出相似度大于 0 的组合。请忽略空文档。为简单起见，可以假定每个文档由一个含有不同整数的数组表示。</p>

<p>输入为一个二维数组 <code>docs</code>，<code>docs[i]</code>&nbsp;表示&nbsp;id 为 <code>i</code> 的文档。返回一个数组，其中每个元素是一个字符串，代表每对相似度大于 0 的文档，其格式为 <code>{id1},{id2}: {similarity}</code>，其中 <code>id1</code> 为两个文档中较小的 id，<code>similarity</code> 为相似度，精确到小数点后 4 位。以任意顺序返回数组均可。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 
<code>[
&nbsp; [14, 15, 100, 9, 3],
&nbsp; [32, 1, 9, 3, 5],
&nbsp; [15, 29, 2, 6, 8, 7],
&nbsp; [7, 10]
]</code>
<strong>输出:</strong>
[
&nbsp; &quot;0,1: 0.2500&quot;,
&nbsp; &quot;0,2: 0.1000&quot;,
&nbsp; &quot;2,3: 0.1429&quot;
]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>docs.length &lt;= 500</code></li>
	<li><code>docs[i].length &lt;= 500</code></li>
</ul>


## thinking

这个题中有个坑，就是浮点数四舍五入导致的问题。[笔记：浮点数的四舍五入](https://app.yinxiang.com/shard/s45/nl/1/39b44589-89c9-4f93-b6a9-c96b66d39507?title=%E6%B5%AE%E7%82%B9%E6%95%B0%E7%9A%84%E5%9B%9B%E8%88%8D%E4%BA%94%E5%85%A5)

## code

```python
from decimal import Decimal

class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        result = []
        i, j = 0, 0
        length = len(docs)
        while i < length:
            j = i + 1
            while j < length:
                merged = set(itertools.chain(docs[i], docs[j]))
                count = len(merged)
                same = len(docs[i]) + len(docs[j]) - count
                if same != 0:
                    pv = Decimal(str(same / float(count))).quantize(Decimal("0.0000"), rounding="ROUND_HALF_UP")
                    result.append(f"{i},{j}: {pv}")
                j += 1
            i += 1
        return result
```