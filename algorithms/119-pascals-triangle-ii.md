# [119. 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/) - easy

<p>给定一个非负索引&nbsp;<em>k</em>，其中 <em>k</em>&nbsp;&le;&nbsp;33，返回杨辉三角的第 <em>k </em>行。</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif"></p>

<p><small>在杨辉三角中，每个数是它左上方和右上方的数的和。</small></p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 3
<strong>输出:</strong> [1,3,3,1]
</pre>

<p><strong>进阶：</strong></p>

<p>你可以优化你的算法到 <em>O</em>(<em>k</em>) 空间复杂度吗？</p>


## thinking


使用 O(k) 空间复杂度，需要从高位往地位计算，因为是上一行的 index 和 index-1 位相加，所以从后往前计算时，需要的信息不会丢失。

![](https://pic.eirture.cn/pics/IMG_8AE519A76FA6-1.jpeg)


## code

第一版本以实现为主：

```golang
func getRow(rowIndex int) []int {
    var results []int
    for i := 0; i <= rowIndex; i++ {
        vs := make([]int, i+1)
        vs[0], vs[i] = 1, 1
        for j := 1; j < i; j++ {
            vs[j] = results[j-1] + results[j]
        }
        results = vs
    }
    return results
}
```

优化，使用两个数组滚动：

```golang
func getRow(rowIndex int) []int {
    r, c := make([]int, rowIndex+1), make([]int, rowIndex+1)

    for i := 0; i <= rowIndex; i++ {
        c[0], c[i] = 1, 1
        for j := 1; j < i; j++ {
            c[j] = r[j-1] + r[j]
        }
        r, c = c, r
    }
    return r
}
```

看了题解思路，使用 O(k) 空间复杂度：

```golang
func getRow(rowIndex int) []int {
    r := make([]int, rowIndex+1)
    r[0] = 1
    for i := 1; i <= rowIndex; i++ {
        for j := i; j > 0; j-- {
            r[j] += r[j-1]
        }
    }
    return r
}
```
