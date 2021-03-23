# [621. 任务调度器](https://leetcode-cn.com/problems/task-scheduler/) - medium

<p>给你一个用字符数组 <code>tasks</code> 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。</p>

<p>然而，两个<strong> 相同种类</strong> 的任务之间必须有长度为整数<strong> </strong><code>n</code><strong> </strong>的冷却时间，因此至少有连续 <code>n</code> 个单位时间内 CPU 在执行不同的任务，或者在待命状态。</p>

<p>你需要计算完成所有任务所需要的<strong> 最短时间</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 2
<strong>输出：</strong>8
<strong>解释：</strong>A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 </pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 0
<strong>输出：</strong>6
<strong>解释：</strong>在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
<strong>输出：</strong>16
<strong>解释：</strong>一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= task.length <= 10<sup>4</sup></code></li>
	<li><code>tasks[i]</code> 是大写英文字母</li>
	<li><code>n</code> 的取值范围为 <code>[0, 100]</code></li>
</ul>


## Solutions

构造一个调用图。

![](https://pic.eirture.cn/pics/893c01db5923889a865d7a4fe71de22b9519fc5a673473196ab58f26c1073ed2-image.png)

找到调用次数最多的任务，次数记为 `maxv`，如果只有这个任务，则需要 `(maxv - 1) * (n + 1) + 1` 单位的时间。如果存在 `maxc` 个 `maxv` 次调用的任务。则需要 `(maxv - 1) * (n + 1) + maxc` 单位的时间。

假设剩下的任务数小于右侧的空闲时间。则这就是最短时间。如果剩下任务数大于右侧空闲时间数。那就可以不需要空闲时间。最短时间等于总的任务个数。

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxv, maxc = 0, 0
        m = {}
        for t in tasks:
            tv = m.get(t, 0)
            tv += 1
            if tv == maxv:
                maxc += 1
            elif tv > maxv:
                maxc = 1
                maxv = tv
            m[t] = tv
        
        n = (maxv - 1) * (n + 1) + maxc
        return max(n, len(tasks)) 
```
