# [100317. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/) - medium

<p>输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。</p>

<p> </p>

<p><strong>示例:</strong><br />
给定如下二叉树，以及目标和 <code>target = 22</code>，</p>

<pre>
              <strong>5</strong>
             / \
            <strong>4</strong>   <strong>8</strong>
           /   / \
          <strong>11</strong>  13  <strong>4</strong>
         /  \    / \
        7    <strong>2</strong>  <strong>5</strong>   1
</pre>

<p>返回:</p>

<pre>
[
   [5,4,11,2],
   [5,8,4,5]
]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>节点总数 <= 10000</code></li>
</ol>

<p>注意：本题与主站 113 题相同：<a href="https://leetcode-cn.com/problems/path-sum-ii/">https://leetcode-cn.com/problems/path-sum-ii/</a></p>


## Solutions

refer to [113. 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)

dfs 又写了一遍

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.rs = []

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.dfs(root, [], target)
        return self.rs

    def dfs(self, n: TreeNode, vs: List, v: int):
        if n is None:
            return

        nv = v - n.val
        nvs = vs + [n.val]
        if n.left is None and n.right is None and nv == 0:
            self.rs.append(nvs)
            return
        self.dfs(n.left, nvs, nv)
        self.dfs(n.right, nvs, nv)

```