# [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) - medium

<p>给定一个长度为 <code>n</code> 的整数数组&nbsp;<code>height</code>&nbsp;。有&nbsp;<code>n</code>&nbsp;条垂线，第 <code>i</code> 条线的两个端点是&nbsp;<code>(i, 0)</code>&nbsp;和&nbsp;<code>(i, height[i])</code>&nbsp;。</p>

<p>找出其中的两条线，使得它们与&nbsp;<code>x</code>&nbsp;轴共同构成的容器可以容纳最多的水。</p>

<p>返回容器可以储存的最大水量。</p>

<p><strong>说明：</strong>你不能倾斜容器。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" /></p>

<pre>
<strong>输入：</strong>[1,8,6,2,5,4,8,3,7]
<strong>输出：</strong>49 
<strong>解释：</strong>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>height = [1,1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Solutions

### 1. 暴力解法

两遍循环，计算每个可能的值，取最大值。时间复杂度 O(n^2)，空间复杂度 O(1)。提交超时了

```go
func maxArea(height []int) int {
    var ma int
    for i := 0; i < len(height)-1 ; i++ {
        for j, h := range height[i+1:] {
            v := min(h, height[i]) * (j+1)
            if ma < v {
                ma = v
            }
        }
    }
    return ma
}
```

### 2. 双指针

左右各一个指针，计算容量取最大值。每次移动更小值的指针。

时间复杂度 O(n)，空间复杂度 O(1)

```go
func maxArea(height []int) int {
    l, h := 0, len(height)-1
    var mv, v int
    for l < h {
        if height[l] <= height[h] {
            v = height[l] * (h - l)
            l++
        } else {
            v = height[h] * (h - l)
            h--
        }
        mv = max(mv, v)
    }
    return mv
}
```
