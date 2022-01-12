## 一、数据结构

需要三个散列表：`graph`、`costs`、`parents`

### graph

```python
# 起点的邻居
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# a节点的邻居
graph['a'] = {}
graph['a']['fin'] = 1

# b节点的邻居
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# 终点没有任何邻居
graph['fin'] = {}
```

因此 `graph[start]` 是一个散列表，起点的邻居可以这样获取：

```python
graph['start'].keys()
```

### costs: 从起点出发，前往该节点需要多长时间

```python
infinity = float('inf')  # 无限大
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
```

### parents：存储父节点

```python
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
```

最后，还需要一个数组，用于记录处理过的节点。



## 二、代码

```python
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果当前节点前往该邻居节点更近
            costs[n] = new_cost  # 更新该邻居的开销
            parents[n] = node    # 同时将当前节点设置为该邻居的父节点
    processed.append(node)
    node = find_lowest_cost_node(costs)
```

查找花销最小的节点

```python
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
```

