# [933. 递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree/) - easy

<p>给你一棵二叉搜索树，请你 <strong>按中序遍历</strong> 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg" style="width: 600px; height: 350px;" />
<pre>
<strong>输入：</strong>root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg" style="width: 300px; height: 114px;" />
<pre>
<strong>输入：</strong>root = [5,1,7]
<strong>输出：</strong>[1,null,5,null,7]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数的取值范围是 <code>[1, 100]</code></li>
	<li><code>0 <= Node.val <= 1000</code></li>
</ul>


## Solutions

### 1. 中序遍历

中序遍历，并记录遍历结果

时间复杂度 O(n)；使用栈做 DFS 空间复杂度 O(n)

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tn = TreeNode()
        self.p = tn
        def dfs(n: TreeNode):
            if n is None:
                return

            dfs(n.left)
            n.left = None
            self.p.right = n
            self.p = n
            dfs(n.right)

        dfs(root)
        return tn.right
```
