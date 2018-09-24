def movierating(arr):
    if len(arr) == 0:   return 0
    first = max(arr[0], 0)
    if len(arr) == 1:   return first
    second = first + second
    ret = max(first, second)
    for i in arr[2:]:
        first, second = second, max(first, second) + i
        ret = max(ret, second)
    return ret