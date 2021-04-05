# [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/) - medium

<p>在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为&ldquo;根&rdquo;。 除了&ldquo;根&rdquo;之外，每栋房子有且只有一个&ldquo;父&ldquo;房子与之相连。一番侦察之后，聪明的小偷意识到&ldquo;这个地方的所有房屋的排列类似于一棵二叉树&rdquo;。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。</p>

<p>计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[3,2,3,null,3,null,1]

     <strong>3</strong>
    / \
   2   3
    \   \ 
     <strong>3</strong>   <strong>1</strong>

<strong>输出:</strong> 7 
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = <strong>7</strong>.</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[3,4,5,1,3,null,1]

&nbsp;    3
    / \
   <strong>4</strong>   <strong>5</strong>
  / \   \ 
 1   3   1

<strong>输出:</strong> 9
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额&nbsp;= <strong>4</strong> + <strong>5</strong> = <strong>9</strong>.
</pre>


## Solutions

### 1. 动态规划


每个节点有两种状态：选择 or 不选择。分别对应可以取得的钱为 f 和 g。

- 选择当前节点，则子节点都不能能选择，有 `f = v + gl + gr`
- 不选择当前节点，子节点可以选择或不选择，有 `f = max(fl, gl) + max(fr, gr)`

最红结果为 `max(froot, groot)`

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(tn: TreeNode):
            if tn == None:
                return 0, 0
            
            fl, gl = dfs(tn.left)
            fr, gr = dfs(tn.right)

            f = tn.val + gl + gr
            g = max(fl, gl) + max(fr, gr)
            return f, g

        return max(*dfs(root))
```

时间复杂度为 O(n); 使用了递归栈，空间复杂度为 O(n)
