# [1000029. 直方图的水量](https://leetcode-cn.com/problems/volume-of-histogram-lcci/) - hard

<p>给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" style="height: 161px; width: 412px;"></p>

<p><small>上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。&nbsp;<strong>感谢 Marcos</strong> 贡献此图。</small></p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>输出:</strong> 6</pre>


## Solutions

### 1. 双指针

l, r 指针，r 往右走，直到 r > l 或者 r == n，如果 r >= l 计算出来的就是他们之间的水量。如果 r == n 说明右侧没有比 l 高的。讲 height[l] 设置为 右侧最高，再走一遍。

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        v = 0
        l = 0
        while l < n:
            r = l + 1
            m = 0
            maxv = 0
            i = l
            while r < n and height[r] < height[l]:
                m += height[l] - height[r]
                maxv = max(maxv, height[r])
                r += 1
            if r == n:
                if height[l] == maxv:
                    l += 1
                else:
                    height[l] = maxv
            else:
                v += m
                l = r
        return v
```

### 2. 单调栈

看了题解思路，还是题解思路清晰。

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        a = []
        result = 0

        for i, h in enumerate(height):
            while a and h > height[a[-1]]:
                top = a.pop()
                if not a:
                    break
                
                l = a[-1]
                width = i - l - 1
                result += (min(height[l], h) - height[top]) * width
            
            a.append(i)
        return result
```
