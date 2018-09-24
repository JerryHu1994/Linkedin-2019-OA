import bisect

def simplequery(arr1, arr2):
	arr1 = sorted(arr1)
	ret = [0]*len(arr2)
	for ind,val in enumerate(arr2):
		ret[ind] = bisect.bisect_right(arr1, val)
	return ret

print simplequery([1,4,2,2,6], [3,5])
