# [530. 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/) - easy

<p>给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>

   1
    \
     3
    /
   2

<strong>输出：</strong>
1

<strong>解释：
</strong>最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中至少有 2 个节点。</li>
	<li>本题与 783 <a href="https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/">https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/</a> 相同</li>
</ul>


## Solutions

相同于：[799. 二叉搜索树节点最小距离](./799-minimum-distance-between-bst-nodes.md)

### 1. 中序遍历

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = 10 ** 5
        self.last = -10 ** 5

        def dfs(n: TreeNode):
            if not n:
                return
            
            dfs(n.left)
            self.ans = min(self.ans, n.val - self.last)
            self.last = n.val
            dfs(n.right)
        
        dfs(root)
        return self.ans
```
