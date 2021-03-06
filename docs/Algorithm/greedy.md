## 贪心算法秘籍

1. 贪心策略

    首先要确定贪心策略，选择当前看上去最好的一个方案。例如，挑选苹果，如果你认为个大的是最好的，那你每次都从苹果堆中拿一个最大。

2. 局部最优解

    根据贪心策略，一步一步地得到局部最优解。例如，第一次选一个最大的苹果放起来，记为 $a_1$，第二次从剩下的苹果中选择最大的一个放起来，记为 $a_2$，以此类推。

3. 把所有的局部最优解合成最优解。例如：挑选一些最好的苹果（$a_1$，$a_2$，...）。



## 最优装载问题—加勒比海盗船

问题：有一天海盗们截获了一艘装满各种各样古董的货船，每一件古董都价值连城，一旦打碎就失去了它的价值。虽然海盗船足够大，但装载重量为 C，每件古董的重量为 $w_i$，海盗们该如何把尽可能多数量的宝贝装上海盗船呢？

### 问题分析

船的载重固定，那么优先把重量小的物品放进去，装的物品最多。采用重量最小者先装的贪心选择策略，从局部最优达到全局最优，从而产生最优装载问题的最优解。

### 算法设计

* 当载重量为 c 时，$w_i$ 越小，可装载的宝贝数量 n 越大。只要依次选择最小重量古董，直到不能再装为止。
* 把 n 个古董的重量从小到大排序，然后根据贪心策略尽可能地选出前 $i$ 个古董，直到不能继续装为止，此时达到最优。

### 伪代码

数据结构，使用一维数组储存古董的重量：

``` python
weight = [……]  # 一维数组存储古董的重量
```

按重量排序

```python
weight.sort()  # 按古董重量升序排序
```

按照贪心策略找最优解

```python
tmp = 0  # tmp代表装载到船上的古董的重量
ans = 0  # ans记录已经装载的古董个数
for i in range(n):
    tmp += weight[i]  # 加上该古董的重量
    if tmp<=c:
        ans ++
    else:
        break
```

### 实战演练

```python
def blocks():
    c,n = eval(input("请输入载重量 c 及古董个数 n，中间用,分隔): "))
    print("载重量c及古董的个数n: {} {}".format(c, n))

    weight = list(eval(input("请输入每个古董的重量，用,分开: ")))
    print("每个古董的重量: {}".format(weight))

    weight.sort()  # 按古董重量升序排序

    tmp = 0  # tmp代表装载到船上的古董的重量
    ans = 0  # ans记录已经装载的古董个数
    for i in range(n):
        tmp += weight[i];
        if tmp<=c:
            ans += 1
        else:
            break

    print("能装入的古董最大数量为 ans={}".format(ans))

if __name__ == "__main__":
    blocks()
```



## 背包问题—阿里巴巴与四十大盗

阿里巴巴跟着强盗发现了一个宝藏，为了让乡亲们开开眼界，见识一下这些宝物，他想一种宝物只拿一个，如果太重就用锤子凿开，但毛驴的运载能力是有限的，怎么才能用驴子运走最大价值的财宝分给穷人呢？阿里巴巴陷入沉思中 ......

### 分析

假设山洞中有 n 中宝物，每种宝物有一定重量 w 和相应的价值 v，毛驴运载能力有限，只能运走 m 重量的宝物，一种宝物只能拿一样，宝物可以分割。那么怎么才能使毛驴运走宝物的价值最大呢？

我们可以尝试贪心策略：每次选取单位重量价值最大的宝物，即性价比最高的宝物。

### 算法设计

* 数据结构及初始化：将 n 种宝物的重量和价值存储载宝物对象中（包含重量、价值、性价比3个属性），同时求出每种宝物的性价比也存储在对应的对象中，最好组成一个由宝物对象组成的列表，并按照性价比从高到低排序。采用 sum 来存储毛驴能够运走的最大价值，初始化为0。
* 根据贪心策略，按照性价比从大到小选取宝物，直到达到毛驴的运载能力。每次选择性价比高的物品，判断是否小于 m （毛驴载重能能力），如果小于 m，则放入，sum 加上当前宝物的价值，m 减去放入宝物的重量；如果不小于 m，则取该宝物的一部分 `m*p[i]`，m=0，程序结束。m 减少到0，则 sum 得到最大值。

### 伪代码

数据结构定义

```python
class Treasure(object):
    
    def __init__(self, w, v p):
        self.w = w  # 宝物的重量
        self.v = v  # 宝物的价值
        self.p = p  # 宝物的性价比
```

性价比排序，需要自定义比较函数，实现宝物性价比的降序排序

```python
def compare(a, b):
    if a.p > b.p:
        return -1
    if a.p < b.p:
        return 1
    return 0

import functools
treasure_list.sort(key=functools.cmp_to_key(compare))  # 使用自定义的比较函数排序
```

贪心算法求解

```python
for i in range(n):
    if m>s[i].w:  # 如果宝物重量小于毛驴剩下的载运能力
        sum += s[i].v
    else:  # 如果宝物重量大于毛驴剩下的载运能力
        sum += m*s[i].p  # 进行宝物切割，使刚好达到驴子承重
        break
```

### 实战演练

```python
import functools

class Treasure(object):

    def __init__(self, w, v, p):
        self.w = w  # 宝物的重量
        self.v = v  # 宝物的价值
        self.p = p  # 宝物的性价比

def compare(a, b):
    # 根据宝物的价值从大到小排序
    return b.p - a.p

def main():
    n = eval(input("请输入宝物的数量n："))
    m = eval(input("请输入毛驴的承重能力m："))

    t_list = []

    for i in range(n):
        w,v = eval(input("请输入宝物的重量和价值，用逗号“,”分隔："))
        t = Treasure(w, v, v/w)  # 构造宝物对象
        t_list.append(t)  # 将宝物对象加入到列表中

    t_list.sort(key=functools.cmp_to_key(compare))
    sum = 0.0  # sum表示贪心记录运走宝物的价值之和
    for i in range(n):
        if m > t_list[i].w:  # 如果宝物的重量小于毛驴剩余载重能力
            m -= t_list[i].w
            sum += t_list[i].v
        else:
            sum += m*t_list[i].p  # 剩余部分
            break
    print("输入宝物的最大价值为：{}".format(sum))

if __name__ == '__main__':
    main()
```



## 会议安排

某跨国公司总裁正分身无术，为一大堆会议时间表焦头烂额，希望钟点秘书能做出合理的安排，能在有限的时间内召开更多的会议。

### 分析

要让会议数最多，我们需要选择最多的不相交时间段。我们可以尝试贪心策略。

1. 每次从剩下未安排的会议中选择会议**具有最早开始时间且与已安排的会议相容**的会议安排，以增大时间的利用率。
2. 每次从剩下未安排的会议中选择**持续时间最短且与已安排的会议相容**的会议安排，这样可以安排更多的会议。
3. 每次从剩下未安排的会议中选择**具有最早结束时间且与已安排的会议相容**的会议安排，这样可以尽快安排下一个会议。

这里我们采用第3种策略。

### 算法设计

* 初始化：将 n 个会议的开始时间、结束时间存放在结构体数组中，如果需要知道选中了哪些会议还需要在结构体中增加会议编号，然后按照结束时间从小到大，结束时间相等时，开开始时间从大到小排序。
* 根据贪心策略就是选择第一个具有最早结束时间的会议，用 last 记录刚选中会议的结束时间；
* 选择第一个会议之后，依次**从剩下未安排的会议中选择**，如果会议 i 开始时间大于等于最后一个选中的会议的结束时间 last，那么会议 i 与已选中的会议相容，可以安排，更新 last 为刚选中会议的结束时间；否则，舍弃会议 i，检查下一个会议是否可以安排。

### 伪代码详解

数据结构定义

```python
class Meet(object):
    def __init__(self, begin, end):
        self.begin = begin  # 会议开始时间
        self.end = end  #会议结束时间
meets = [Meet(x1, y1), Meet(x2, y2)..., Meet(xn,yn)]
```

对会议按照结束时间非递减排序

```python
def compare(a, b):
    if a.end == b.end:  # 结束时间相等
        return a.begin - b.begin  # 按开始时间从大到小排序
    return b.end - a.end:  # 按结束时间从小到大排序

import functools
meets.sort(key=functools.cmp_to_key(compare))  # 使用自定义的比较函数排序
```

会议安排问题的贪心算法求解

```python
ans = 1  # 用来记录可以安排会议的个数，初始时选中了第一个会议
last = meets[0].end  # last记录第一个会议的结束时间
# 依次检查每个会议
for i in range(1, n):
    if meets[i].begin >= last:
        # 如果会议i开始时间大于等于最后一个选中的会议的结束时间
        ans++
        last = meets[i].end  # 更新last为最后一个选中会议的结束时间
return ans  # 返回可以安排的会议最大数
```

### 实战演练

```python
import functools

class Meet(object):

    def __init__(self, begin, end, num):
        self.begin = begin  # 会议开始时间
        self.end = end  # 会议结束时间
        self.num = num   # 会议编号

def compare(a, b):
    if a.end == b.end:  # 结束时间相等
        return b.begin - a.begin  # 按开始时间从大到小排序
    return a.end - b.end  # 按结束时间从小到大排序


class SetMeet(object):

    def __init__(self):
        n = eval(input('输入会议总数：'))
        meets = []  # 存放会议的列表
        for i in range(n):
            start, end = eval(input('输入会议开始时间和结束时间，以‘,’分隔：'))
            meets.append(Meet(start, end, i+1))
        self.n = n
        self.meets = meets
        self.ans = 1

    def solve(self):
        self.meets.sort(key=functools.cmp_to_key(compare))  # 对会议排序

        print('选择会议过程：')
        last = self.meets[0].begin  # 记录刚刚被选中会议的结束时间
        for m in self.meets:
            if m.begin>=last:
                self.ans += 1
                last = m.end
                print('选择第{}个会议'.format(m.num))
        print('最多可以安排{}个会议'.format(self.ans))

def main():
    sm = SetMeet()  # 读入数据
    sm.solve()  # 贪心算法求解


if __name__ == '__main__':
    main()
```



