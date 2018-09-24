def distinctpairs(arr, target):
    cnt = collections.defaultdict(int)
    for i in arr:   cnt[i] += 1
    keys = sorted(cnt.keys())
    ret = 0
    print keys, target
    for k in keys:
        if k > target//2:
            return ret
        if target % 2 == 0 and k == target/2:
            if cnt[target/2] >= 2:
                ret += 1
                continue
        else:
            if target-k in cnt:
                ret += 1
    return ret