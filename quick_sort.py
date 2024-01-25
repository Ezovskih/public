процессорный 

def partition(l, r):
    pivot = a[random(l ... r - 1)]
    m = l
    for i = l ... r - 1:
        if a[i] < pivot:
            swap(a[i], a[m])
            m++
    return m

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [3,6,8,10,1,2,1]
print(quicksort(arr))
