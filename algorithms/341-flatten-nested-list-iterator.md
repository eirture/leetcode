# [341. 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator/) - medium

<p>给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。</p>

<p>列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[[1,1],2,[1,1]]
<strong>输出: </strong>[1,1,2,1,1]
<strong>解释: </strong>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[1,[4,[6]]]
<strong>输出: </strong>[1,4,6]
<strong>解释: </strong>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回 false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>。
</pre>


## Solutions

递归做 DFS。利用 Python 原生的迭代器，避免额外的存储空间，但是其实也需要保存栈的信息。时间复杂度 O(n)

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.g = iterator(nestedList)
        self.n = None

    
    def next(self) -> int:
        v = self.n
        if v is None:
            return next(self.g)
        self.n = None
        return v
    
    def hasNext(self) -> bool:
        if self.n is not None:
            return True
        try:
            self.n = next(self.g)
        except StopIteration:
            return False
        return True

def iterator(nl):
    for n in nl:
        if n.isInteger():
            yield n.getInteger()
        else:
            for i in iterator(n.getList()):
                yield i

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

贴合题目中给出的调用方式，可以更精简一些：
```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.g = iterator(nestedList)
        self.n = None

    def next(self) -> int:
        v, self.n = self.n, None
        return v
    
    def hasNext(self) -> bool:
        try:
            self.n = next(self.g)
        except StopIteration:
            return False
        return True

def iterator(nl):
    for n in nl:
        if n.isInteger():
            yield n.getInteger()
        else:
            for i in iterator(n.getList()):
                yield i
```