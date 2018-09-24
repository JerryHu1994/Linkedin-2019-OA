def cutsticks(arr):
	arr = sorted(arr)
	ret = []
	for i in range(1, len(arr)):
		if arr[i] != arr[i-1]:
			ret.append(len(arr)-i)
	return ret

print cutsticks([1,2,3,4,4,5,6])