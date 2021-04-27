# [975. 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst/) - easy

<p>给定二叉搜索树的根结点 <code>root</code>，返回值位于范围 <em><code>[low, high]</code></em> 之间的所有结点的值的和。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;" />
<pre>
<strong>输入：</strong>root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>输出：</strong>32
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;" />
<pre>
<strong>输入：</strong>root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>输出：</strong>23
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 2 * 10<sup>4</sup>]</code> 内</li>
	<li><code>1 <= Node.val <= 10<sup>5</sup></code></li>
	<li><code>1 <= low <= high <= 10<sup>5</sup></code></li>
	<li>所有 <code>Node.val</code> <strong>互不相同</strong></li>
</ul>


## Solutions

### 1. DFS

深度优先遍历，判断当前节点值 v 与 `low`, `high` 关系。

- 如果 `low <= v <= high` 则有：sumv = n.v + dfs(n.left) + dfs(n.right)
- `v < low` 则有：sumv = dfs(n.right)
- `v > high` 则有：sumv = dfs(n.left)


```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        if root is None:
            return 0
        
        v = root.val
        if v >= low and v <= high:
            return v + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif v > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)
```
