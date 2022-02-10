核心：通过构建有序序列，对于未排序序列，在已排序序列中从后向前扫描(对于单向链表则只能从前往后遍历)，找到相应位置并插入。实现上通常使用 in-place 排序(需用到O(1)的额外空间)

1. 从第一个元素开始，该元素可认为已排序
2. 取下一个元素，对已排序数组从后往前扫描
3. 若从排序数组中取出的元素大于新元素，则移至下一位置
4. 重复步骤3，直至找到已排序元素小于或等于新元素的位置
5. 插入新元素至该位置
6. 重复2~5

![](../img/insertion_sort.gif)

```python
#!/usr/bin/env python


def insertionSort(alist):
    for i, item_i in enumerate(alist):
        print(alist)
        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i

    return alist

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionSort(unsorted_list))
```

