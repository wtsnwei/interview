将数组元素按从小到大的顺序排列。

1、先编写一个用于找出数组中最小元素的函数。

```python
def findSmallest(arr):
    smallest = arr[0]  # 存储最小的值
    smallest_index = 0  # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
```



2、选择排序

```python
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # 找出数组中最小的元素，并将其加入到新数组中
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, 3, 6, 2, 10])
```

3、性能

需要的总时间为 $O(n \times n)$，即 $O(n^2)$。