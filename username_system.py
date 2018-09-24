def usernamesystem(arr):
    cnt = collections.defaultdict(int)
    for ind,val in enumerate(arr):
        if cnt[val] == 0:
            cnt[val] = 1
        else:
            arr[ind] = val+str(cnt[val])
            cnt[val] += 1
    return arr