# [437. 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii/) - medium

<p>给定一个二叉树，它的每个结点都存放着一个整数值。</p>

<p>找出路径和等于给定数值的路径总数。</p>

<p>路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。</p>

<p>二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。</p>

<p><strong>示例：</strong></p>

<pre>root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    <strong>5</strong>   <strong>-3</strong>
   <strong>/</strong> <strong>\</strong>    <strong>\</strong>
  <strong>3</strong>   <strong>2</strong>   <strong>11</strong>
 / \   <strong>\</strong>
3  -2   <strong>1</strong>

返回 3。和等于 8 的路径有:

1.  5 -&gt; 3
2.  5 -&gt; 2 -&gt; 1
3.  -3 -&gt; 11
</pre>


## Solutions


### DFS + 前缀和

看见“路径和”就应该要想到“前缀和”。

```python
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(n: TreeNode, pss: list) -> int:
            if n is None:
                return 0

            ps = pss[-1] + n.val
            l = 0
            nc = 0
            while l < len(pss):
                if ps - pss[l] == sum:
                    nc += 1
                l += 1

            return nc + dfs(n.left, pss + [ps]) + dfs(n.right, pss + [ps])
        
        prefix_sum = [0]
        return dfs(root, prefix_sum)
```

可以优化一下前缀和，使用一个 map 存储前缀和为 v 的个数。

```python
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(n: TreeNode, pres: int, prefix_sum: map) -> int:
            if n is None:
                return 0

            ps = pres + n.val

            nc = prefix_sum[ps - sum]
            prefix_sum[ps] += 1

            return nc + dfs(n.left, ps, prefix_sum.copy()) + dfs(n.right, ps, prefix_sum.copy())
        
        prefix_sum = defaultdict(lambda: 0)
        prefix_sum[0] = 1
        return dfs(root, 0, prefix_sum)

```

这里还可以优化，由于执行是线性的，当前节点的前缀和只对本节点一下节点有效。所以可以在本节点退出的时候，将本节点从 m 中摘掉。这样就不需要复制 m。


```python
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(n: TreeNode, pres: int, prefix_sum: map) -> int:
            if n is None:
                return 0

            ps = pres + n.val

            nc = prefix_sum[ps - sum]
            prefix_sum[ps] += 1

            nc += dfs(n.left, ps, prefix_sum)
            nc += dfs(n.right, ps, prefix_sum)

            # 退出之前，摘掉本节点前缀和
            prefix_sum[ps] -= 1
            return nc

        prefix_sum = defaultdict(lambda: 0)
        prefix_sum[0] = 1
        return dfs(root, 0, prefix_sum)
```