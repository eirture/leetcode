# [799. 二叉搜索树节点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/) - easy

<p>给你一个二叉搜索树的根节点 <code>root</code> ，返回 <strong>树中任意两不同节点值之间的最小差值</strong> 。</p>

<p><strong>注意：</strong>本题与 530：<a href="https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/">https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/</a> 相同</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [4,2,6,1,3]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [1,0,48,null,null,12,49]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[2, 100]</code> 内</li>
	<li><code>0 <= Node.val <= 10<sup>5</sup></code></li>
</ul>
</div>
</div>


## Solutions

### 1. 深度遍历

这个题目因为是一个搜索树，已经有序，难度不大。获取左侧最大，右侧最小，与当前节点求差。

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        vs = []

        def dfs(n: TreeNode):
            if n.left:
                l = n.left
                while l.right:
                    l = l.right
                vs.append(n.val - l.val)
                dfs(n.left)
            
            if n.right:
                r = n.right
                while r.left:
                    r = r.left
                vs.append(r.val - n.val)
                dfs(n.right)

        dfs(root)
        return min(vs)
```

### 2. 中序遍历

中序遍历就能顺序遍历所有节点。求任意两节点差值最小，一定是有序相邻的两节点。

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ans = 10 ** 5
        self.last = -10 ** 5

    def minDiffInBST(self, root: TreeNode) -> int:
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
