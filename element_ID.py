import collections
def elementID(arr):
	pairs = [(ind, val) for ind, val in enumerate(arr)]
	pairs = sorted(pairs, key = lambda x:[-x[1], x[0]])
	ret = []
	while len(pairs) >= 3:
		ret.append([p[0] for p in pairs[:3]])
		pairs = pairs[3:]
	if pairs > 0:
		ret.append([p[0] for p in pairs])
	return ret

print elementID([3,3,3,3,3,1,3])