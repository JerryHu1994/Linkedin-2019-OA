def maxDiff(arr):
    ret, currmin = float("-inf"), float("inf")
    for num in arr:
        currmin = min(currmin, num)
        ret = max(num - currmin, ret)
    return -1 if ret < 0 else ret