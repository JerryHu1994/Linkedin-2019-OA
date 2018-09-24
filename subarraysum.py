def subarraysum(arr):
    ret, l = 0, len(arr)
    for ind, val in enumerate(arr):
        start, end, middle = l - ind, ind, ind*(l-1-ind)
        ret += val*(start+end+middle)
    return ret