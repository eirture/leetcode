# [543. 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/) - easy

<p>给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。</p>

<p>&nbsp;</p>

<p><strong>示例 :</strong><br>
给定二叉树</p>

<pre>          1
         / \
        2   3
       / \     
      4   5    
</pre>

<p>返回&nbsp;<strong>3</strong>, 它的长度是路径 [4,2,1,3] 或者&nbsp;[5,2,1,3]。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong>两结点之间的路径长度是以它们之间边的数目表示。</p>


## Solutions

DFS

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    var dfs func(n *TreeNode) int
    max := 0
    dfs = func(n *TreeNode) int {
        if n == nil {
            return -1
        }
        l := dfs(n.Left) + 1
        r := dfs(n.Right) + 1
        if max < l + r {
            max = l + r
        }
        if l > r {
            return l
        }
        return r
    }
    dfs(root)
    return max
}
```