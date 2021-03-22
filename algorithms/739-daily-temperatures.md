# [739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/) - medium

<p>请根据每日 <code>气温</code> 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用&nbsp;<code>0</code> 来代替。</p>

<p>例如，给定一个列表&nbsp;<code>temperatures = [73, 74, 75, 71, 69, 72, 76, 73]</code>，你的输出应该是&nbsp;<code>[1, 1, 4, 2, 1, 1, 0, 0]</code>。</p>

<p><strong>提示：</strong><code>气温</code> 列表长度的范围是&nbsp;<code>[1, 30000]</code>。每个气温的值的均为华氏度，都是在&nbsp;<code>[30, 100]</code>&nbsp;范围内的整数。</p>


## Solutions

### 1. 单调栈

将 index 保存在一个栈中，遍历 T， 并与栈顶 index 比较。index 查就是相隔天数。

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        a = []
        results = []
        for i, v in enumerate(T):
            results.append(0)
            
            while a and T[a[-1]] < v:
                ti = a.pop()
                results[ti] = (i - ti)
            a.append(i)
        for i in a:
            results[i] = 0

        return results
```