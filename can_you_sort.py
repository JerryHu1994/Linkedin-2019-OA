import collections

def canyousort(arr):
	cnt = collections.defaultdict(int)
	for i in arr:	cnt[i] += 1
	pairs = [(key, value) for key,value in cnt.iteritems()]
	pairs = sorted(pairs, key = lambda x: [x[1], x[0]])
	ret = []
	for p in pairs:	ret += [p[0]]*p[1]
	return ret

print canyousort([4,5,6,5,4,3])