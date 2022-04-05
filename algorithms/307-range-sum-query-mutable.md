# [307. 区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable/) - medium

<p>给你一个数组 <code>nums</code> ，请你完成两类查询。</p>

<ol>
	<li>其中一类查询要求 <strong>更新</strong> 数组&nbsp;<code>nums</code>&nbsp;下标对应的值</li>
	<li>另一类查询要求返回数组&nbsp;<code>nums</code>&nbsp;中索引&nbsp;<code>left</code>&nbsp;和索引&nbsp;<code>right</code>&nbsp;之间（&nbsp;<strong>包含&nbsp;</strong>）的nums元素的 <strong>和</strong>&nbsp;，其中&nbsp;<code>left &lt;= right</code></li>
</ol>

<p>实现 <code>NumArray</code> 类：</p>

<ul>
	<li><code>NumArray(int[] nums)</code> 用整数数组 <code>nums</code> 初始化对象</li>
	<li><code>void update(int index, int val)</code> 将 <code>nums[index]</code> 的值 <strong>更新</strong> 为 <code>val</code></li>
	<li><code>int sumRange(int left, int right)</code> 返回数组&nbsp;<code>nums</code>&nbsp;中索引&nbsp;<code>left</code>&nbsp;和索引&nbsp;<code>right</code>&nbsp;之间（&nbsp;<strong>包含&nbsp;</strong>）的nums元素的 <strong>和</strong>&nbsp;（即，<code>nums[left] + nums[left + 1], ..., nums[right]</code>）</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
<strong>输出</strong>：
[null, 9, null, 8]

<strong>解释</strong>：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 *&nbsp;10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index &lt; nums.length</code></li>
	<li><code>-100 &lt;= val &lt;= 100</code></li>
	<li><code>0 &lt;= left &lt;= right &lt; nums.length</code></li>
	<li>调用 <code>update</code> 和 <code>sumRange</code> 方法次数不大于&nbsp;<code>3 * 10<sup>4</sup></code>&nbsp;</li>
</ul>


## Solutions

### 1. 前缀和

第一想到的办法是，用一个数组 sums[i] 记录 nums[0] + ... nums[i] 和。查询 nums[l] + ... nums[r] 可以转化为 sums[r] - sums[l-1]。但是每次更新需要维护 sums。

空间复杂度为 O(n)；时间复杂度 Constructor is O(n); Update is O(n); SumRange is O(1);

```go
type NumArray struct {
    nums []int
    sums []int
}


func Constructor(nums []int) NumArray {

    sums := make([]int, len(nums)+1)
    for i, n := range nums {
        sums[i+1] = sums[i] + n
    }

    return NumArray{
        nums: nums,
        sums: sums,
    }
}


func (this *NumArray) Update(index int, val int)  {
    detal := val - this.nums[index]
    this.nums[index] = val

    for i := index; i < len(this.nums); i++ {
        this.sums[i + 1] += detal
    }
}


func (this *NumArray) SumRange(left int, right int) int {
    return this.sums[right+1] - this.sums[left]
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
```

### 分块处理

分块处理，是把数抽象了一下，多个数据当作一个数据来处理。这样做，在查询范围的时候，需要将边界数据拆开，来重新算一遍。

至于快的大小是多少合适？题解中给的答案是 sqrt(n)。这个是根据 SumRange 的时间复杂度 O(size + n / size) 来推到出来的。size <= n 有 size + n / size >= sqrt(n). 当且仅当 size == sqrt(n) 是否。O(size + n / size) 最小，为 O(sqrt(n))

空间复杂度为 O(size) = O(sqrt(n))
时间复杂度为，Constructor O(n); Update O(1); SumRange O(sqrt(n)).

```go
type NumArray struct {
	nums []int
	sums []int
	size int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	size := int(math.Ceil(math.Sqrt(float64(n))))
	sums := make([]int, int(math.Ceil(float64(n)/float64(size))))

	for i, v := range nums {
		sums[i/size] += v
	}

	return NumArray{
		nums: nums,
		sums: sums,
		size: size,
	}
}

func (this *NumArray) Update(index int, val int) {
	this.sums[index/this.size] += val - this.nums[index]
	this.nums[index] = val
}

func (this *NumArray) SumRange(left int, right int) int {
	bl := left / this.size
	br := right / this.size

	if bl == br {
		return sum(this.nums, left, right+1)
	}
	return sum(this.nums, left, (bl+1)*this.size) + sum(this.sums, bl+1, br) + sum(this.nums, br*this.size, right+1)
}

func sum(ns []int, i, j int) int {
	sum := 0
	for i < j {
		sum += ns[i]
		i++
	}
	return sum
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */

```


### 线段树

用一颗完全二叉树记录元素和。[线段树介绍](https://baike.baidu.com/item/%E7%BA%BF%E6%AE%B5%E6%A0%91/10983506)

```go
type NumArray struct {
	seg []int
	n   int
}

func Constructor(nums []int) NumArray {
	n := len(nums)

	na := NumArray{
		seg: make([]int, 4*n),
		n:   n,
	}
	na.build(nums, 0, 0, n-1)
	return na
}

func (this *NumArray) build(nums []int, node, l, r int) {
	if l == r {
		this.seg[node] = nums[l]
		return
	}

	m := l + (r-l)/2
	this.build(nums, node*2+1, l, m)
	this.build(nums, node*2+2, m+1, r)
	this.seg[node] = this.seg[node*2+1] + this.seg[node*2+2]
}

func (this *NumArray) change(i, node, val, l, r int) {
	if l == r {
		this.seg[node] = val
		return
	}

	m := l + (r-l)/2
	if i <= m {
		this.change(i, node*2+1, val, l, m)
	} else {
		this.change(i, node*2+2, val, m+1, r)
	}
	this.seg[node] = this.seg[node*2+1] + this.seg[node*2+2]
}

func (this *NumArray) Range(s, e, node, l, r int) int {
	if s == l && e == r {
		return this.seg[node]
	}
	m := l + (r-l)/2
	if e <= m {
		return this.Range(s, e, node*2+1, l, m)
	}
	if s > m {
		return this.Range(s, e, node*2+2, m+1, r)
	}

	return this.Range(s, m, node*2+1, l, m) + this.Range(m+1, e, node*2+2, m+1, r)
}

func (this *NumArray) Update(index int, val int) {
	this.change(index, 0, val, 0, this.n-1)
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.Range(left, right, 0, 0, this.n-1)
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
```