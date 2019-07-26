# Order Statistics

## Median 

The time complexity of this algorithm is:

$$O(nlog(n))$$

```python

def nlogn_median(lst):
    median = None
    if len(lst) > 0:
        lst.sort()
        median = (lst[len(lst)//2] + lst[~(len(lst)//2)]) / 2.
    return median
```

## Partition

Places value located at $\mathbf{\mbox{lst}[\mbox{right}]}$ in **lst** as position **idx** such that:

$$\mbox{lst}[\mbox{idx}] \lt \mbox{lst}[\mbox{idx+1:}]$$

$$\mbox{lst}[\mbox{idx}] \gt \mbox{lst}[\mbox{:left}]$$

```python
def partition(lst, left, right):
    if len(lst) == 0:
        return None

    pivot = lst[right]
    i = left - 1

    for j in range(right):
        if lst[j] < pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i+1
```

!!! Example
    ```python
        ary = [0, 1, 6, 7, 4]
        pivot_index = subject.partition(ary, 0, 4)

        pivot_index # 2
        ary # [0, 1, 4, 7, 6]
    ```