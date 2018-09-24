def paritypermutation(n):
    nlist = [i for i in range(1, n+1)]
    ret = []
    # True for even, False for odd
    def dfs(li, parity, currlist):
        if len(currlist) == n:
            ret.append(currlist)
        for i in li:
            if i in currlist:   continue
            if (i%2==0 and not parity) or (i%2==1 and parity):
                dfs(li, not parity, currlist+[i])
    for i in range(1, n+1):
        dfs(nlist, i%2==0, [i])
    return ret